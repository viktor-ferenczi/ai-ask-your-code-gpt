import asyncio
import json
import os
from traceback import print_exc
from typing import Dict

import quart
import quart_cors
from quart import request, Response

from common.constants import C, RX
from common.server import run_app
from project.inventory import Inventory
from project.project import Project, ProjectError
from common.tools import tiktoken_len

MODULE_DIR = os.path.dirname(__file__)
AI_PLUGIN_PATH = os.path.join(MODULE_DIR, 'ai-plugin.json')
OPENAPI_YAML_PATH = os.path.join(MODULE_DIR, 'openapi.yaml')

DEVELOPMENT_HTTP_PORT = 5555


def html_prod_to_dev(text):
    text = text.replace('"AskYourCode"', '"AskYourCodeDev"')
    text = text.replace('"askyourcode"', '"askyourcodedev"')
    text = text.replace('https://askyourcode.ai', f'http://localhost:{DEVELOPMENT_HTTP_PORT}')
    text = text.replace('https://plugin.askyourcode.ai', f'http://localhost:{DEVELOPMENT_HTTP_PORT}')
    return text


app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")


@app.get("/")
async def index():
    return await quart.send_file('index.html', mimetype='text/html')


@app.get("/logo.png")
async def logo():
    return await quart.send_file('logo.png', mimetype='image/png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    with open(AI_PLUGIN_PATH, 'rt') as f:
        text = f.read()
    if C.DEVELOPMENT:
        text = html_prod_to_dev(text)
    return Response(text, mimetype="text/json", status=200)


@app.get("/openapi.yaml")
async def openapi_spec():
    with open(OPENAPI_YAML_PATH, 'rt') as f:
        text = f.read()
    if C.DEVELOPMENT:
        text = html_prod_to_dev(text)
    return Response(text, mimetype="text/yaml", status=200)


# noinspection HttpUrlsUsage
@app.post("/project")
async def create():
    body: Dict[str, str] = await quart.request.get_json(force=True)

    # Validate URL
    url: str = body.get('url')
    if not url:
        return Response(response='Missing url', status=400)
    if not (url.startswith('http://') or url.startswith('https://')):
        return Response(response='The URL must start with http:// or https://', status=400)

    if url.startswith('https://www.dropbox.com/') and url.endswith('?dl=0'):
        url = f'{url[:-5]}?dl=1'

    lc_url = url.lower()
    if C.PRODUCTION and ('://localhost' in lc_url or '://127.' in url or '://192.168.' in url or '://10.' in url):
        return Response(response='Invalid URL', status=400)
    if 'https://drive.google.com/' in lc_url or 'https://1drv.ms/' in lc_url:
        return Response(response='Google Drive and OneDrive are not supported, Dropbox works. The URL must point to a publicly and directly downloadable ZIP file. Please use a GitHub ZIP download link or a direct file link from Discord. Please find the FAQ, HowTo and bug-reports at https://askyourcode.ai', status=400)

    # Create project, download and verify archive, initiate indexing
    print(f'Create project from {url!r}')

    # noinspection PyBroadException
    try:
        project_id = await Project.download(url)
    except KeyboardInterrupt:
        raise
    except ProjectError as e:
        return Response(response=f'{e}; Please find the FAQ, HowTo and bug-reports at https://askyourcode.ai', status=400)
    except Exception:
        print(f'ERROR: Failed to create project from archive URL {url!r}')
        print_exc()
        return Response(response='Failed to create project; Please find the FAQ, HowTo and bug-reports at https://askyourcode.ai', status=400)

    project = Project(project_id)
    response = dict(
        project_id=project_id,
        progress=project.progress
    )
    return Response(response=json.dumps(response, indent=2), status=200)


@app.delete("/project/<string:project_id>")
async def delete(project_id: str):
    project_id = project_id.lower()
    if not RX.GUID.match(project_id):
        return Response(response='Invalid project_id, it must be a GUID', status=400)

    print(f'Delete project {project_id!r}')

    # noinspection PyBroadException
    try:
        project = Project(project_id)
        await project.delete()
    except KeyboardInterrupt:
        raise
    except ProjectError as e:
        print(f'Failed to delete project {project_id!r}: {e}')
        return Response(response=str(e), status=400)
    except Exception:
        print(f'ERROR: Failed to delete project {project_id!r}')
        print_exc()
        return Response(response='Failed to delete project, please try again later', status=500)

    return Response(response='OK', status=200)


@app.get("/project/<string:project_id>/summarize")
async def summarize(project_id: str):
    # noinspection DuplicatedCode
    project_id = project_id.lower()
    if not RX.GUID.match(project_id):
        return Response(response='Invalid project_id, it must be a GUID', status=400)

    path: str = request.args.get('path', '')
    tail: str = request.args.get('tail', '')
    name: str = request.args.get('name', '')

    if path in ('/', '.'):
        path = ''

    print(f'Summarize project {project_id!r}: path={path!r}, tail={tail!r}, name={name!r}')

    inventory = Inventory()
    project = Project(project_id)
    if not project.exists:
        url = inventory.get_project_url(project_id)
        if not url:
            return Response(response='No such project', status=404)
        await project.download(url)
        for _ in range(10):
            await asyncio.sleep(1.0)
            if inventory.has_project_extracted(project_id):
                break

    if not project.exists:
        return Response(response='No such project', status=404)

    inventory.touch_project(project_id)

    # noinspection PyBroadException
    try:
        text = await project.summarize(path=path, tail=tail, name=name)
    except KeyboardInterrupt:
        raise
    except ProjectError as e:
        print(f'Failed to summarize project {project_id!r}: {e}')
        print(f'- path={path!r}')
        print(f'- tail={tail!r}')
        print(f'- name={name!r}')
        return Response(response=str(e), status=400)
    except Exception:
        print(f'ERROR: Failed to summarize project {project_id!r}')
        print(f'- path={path!r}')
        print(f'- tail={tail!r}')
        print(f'- name={name!r}')
        print_exc()
        return Response(response='Failed to summarize, please try again later', status=500)

    if not text:
        return Response(response='No match found', status=204)

    if not path and not tail and not name:
        text = f'''
High level documentation and code references in the project as a starting point:
        
{text}
        
'''

    # Summarize the classes or functions of interest before trying to search for actual code.
    # Use the path, tail, name and text search parameters to narrow down your lookups.
    # Try again with a more relaxed search condition if you don't get a result.
    # Use the name search to find class, function, method and variable definitions.
    # Use the text search to find their usages in code.

    return Response(response=text, status=200)


@app.get("/project/<string:project_id>/search")
async def search(project_id: str):
    # noinspection DuplicatedCode
    project_id = project_id.lower()
    if not RX.GUID.match(project_id):
        return Response(response='Invalid project_id, it must be a GUID', status=400)

    path: str = request.args.get('path', '')
    tail: str = request.args.get('tail', '')
    name: str = request.args.get('name', '')
    text: str = request.args.get('text', '')

    print(f'Search project {project_id!r}: path={path!r}, tail={tail!r}, name={name!r}, text={text!r}')

    inventory = Inventory()
    project = Project(project_id)
    if not project.exists:
        url = inventory.get_project_url(project_id)
        if not url:
            return Response(response='No such project', status=404)
        await project.download(url)
        for _ in range(10):
            await asyncio.sleep(1.0)
            if inventory.has_project_extracted(project_id):
                break

    if not project.exists:
        return Response(response='No such project', status=404)

    inventory.touch_project(project_id)

    if path and not path.startswith('/'):
        path = f'/{path}'

    if path and tail and not name:
        path = f'{path.rstrip("/")}/{tail.lstrip("/")}'
        tail = ''

    if path and name and not tail:
        path = f'{path.rstrip("/")}/{name.lstrip("/")}'
        name = ''

    limit = 10
    if path or tail or name:
        limit = 50

    # noinspection PyBroadException
    try:
        hits = await project.search(path=path, tail=tail, name=name, text=text, limit=limit)
        if not hits and name:
            hits = await project.search(path=path, tail=tail, text=name, limit=limit)
            if not hits:
                hits = await project.search(tail=tail, text=name, limit=limit)
            if not hits:
                hits = await project.search(text=name, limit=10)
        if not hits and path:
            hits = await project.search(tail='/' + path.rsplit('/')[-1], text=text, limit=limit)
    except KeyboardInterrupt:
        raise
    except ProjectError as e:
        print(f'Failed to search project {project_id!r}: {e}')
        print(f'- path={path!r}')
        print(f'- tail={tail!r}')
        print(f'- name={name!r}')
        print(f'- text={text!r}')
        return Response(response=str(e), status=400)
    except Exception:
        print(f'ERROR: Failed to search project {project_id!r}')
        print(f'- path={path!r}')
        print(f'- tail={tail!r}')
        print(f'- name={name!r}')
        print(f'- text={text!r}')
        print_exc()
        return Response(response='Failed to search the project contents. Please try again later.', status=500)

    if not hits:
        return Response(response='No match found', status=204)

    path = hits[0].path

    if text:
        hits = hits[:1]
    else:
        hits = [hit for hit in hits if hit.path == path]
        hits.sort(key=lambda hit: hit.lineno)

        tokens = tiktoken_len(hits[0].text)
        i = 1
        while i < len(hits):
            tokens += tiktoken_len(hits[i].text)
            if tokens > 2000:
                break
            i += 1

        hits = hits[:i]

    response = dict(
        path=path,
        lineno=hits[0].lineno,
        text='\n'.join(hit.text for hit in hits),
    )

    for hit in hits:
        if hit.name:
            response['name'] = name
            break

    if project.progress < 100:
        response['progress'] = project.progress

    return Response(response=json.dumps(response, indent=2), status=200)


if __name__ == "__main__":
    asyncio.run(run_app(app, debug=C.DEVELOPMENT, host="localhost", port=DEVELOPMENT_HTTP_PORT))

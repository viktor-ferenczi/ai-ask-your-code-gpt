import asyncio
import json
import os
import time
import uuid
from traceback import print_exc
from typing import Dict

import quart
import quart_cors
from quart import request, Response

from common.constants import C, RX
from common.server import run_app
from project.project import Project, ProjectError

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
    deadline = time.time() + C.MAX_WAIT_TIME_AFTER_DOWNLOAD

    body: Dict[str, str] = await quart.request.get_json(force=True)

    # Validate URL
    url: str = body.get('url')
    if not url:
        return Response(response='Missing url', status=400)
    if not (url.startswith('http://') or url.startswith('https://')):
        return Response(response='The URL must start with http:// or https://', status=400)
    if C.PRODUCTION and ('://localhost' in url.lower() or '://127.' in url or '://192.168.' in url or '://10.' in url):
        return Response(response='Invalid URL', status=400)

    # Create project, download and verify archive, initiate indexing
    project_id = str(uuid.uuid4())
    print(f'Create project {project_id!r} from {url!r}')

    # noinspection PyBroadException
    try:
        project = Project(project_id)
        await project.download(url)
    except KeyboardInterrupt:
        raise
    except ProjectError as e:
        print(f'Failed to download project {project_id!r}: {e}')
        return Response(response=str(e), status=400)
    except Exception:
        print(f'ERROR: Failed to create project {project_id!r} from archive URL {url!r}')
        print_exc()
        return Response(response='Failed to create project', status=400)

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
    project_id = project_id.lower()
    if not RX.GUID.match(project_id):
        return Response(response='Invalid project_id, it must be a GUID', status=400)

    path: str = request.args.get('path', '')
    tail: str = request.args.get('tail', '')
    name: str = request.args.get('name', '')

    if path in ('/', '.'):
        path = ''

    print(f'Summarize project {project_id!r}: path={path!r}, tail={tail!r}, name={name!r}')

    project = Project(project_id)
    if not project.exists:
        return Response(response='No such project', status=404)

    try:
        text = await project.summarize(path, tail, name)
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

    return Response(response=text, status=200)


@app.get("/project/<string:project_id>/search")
async def search(project_id: str):
    project_id = project_id.lower()
    if not RX.GUID.match(project_id):
        return Response(response='Invalid project_id, it must be a GUID', status=400)

    path: str = request.args.get('path', '')
    tail: str = request.args.get('tail', '')
    name: str = request.args.get('name', '')
    text: str = request.args.get('text', '')

    print(f'Search project {project_id!r}: path={path!r}, tail={tail!r}, name={name!r}, text={text!r}')

    project = Project(project_id)
    if not project.exists:
        return Response(response='No such project', status=404)

    try:
        hits = await project.search(path, tail, name, text)
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

    hit = hits[0]

    response = dict(
        path=hit.path,
        lineno=hit.lineno,
        text=hit.text,
    )

    if hit.name:
        response['name'] = hit.name

    if project.progress < 100:
        response['progress'] = hit.progress

    return Response(response=json.dumps(response, indent=2), status=200)


if __name__ == "__main__":
    asyncio.run(run_app(app, debug=C.DEVELOPMENT, host="localhost", port=DEVELOPMENT_HTTP_PORT))

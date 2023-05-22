import json
import os
import sys
import uuid
from traceback import print_exc
from typing import Dict

import quart
import quart_cors
from quart import request

from project import Project, ProjectException

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

_TODOS = {}

DEVELOPMENT = sys.platform == 'win32'

MODULE_DIR = os.path.dirname(__file__)
AI_PLUGIN_PATH = os.path.join(MODULE_DIR, 'ai-plugin.json')
OPENAPI_YAML_PATH = os.path.join(MODULE_DIR, 'openapi.yaml')

PORT = int(os.environ.get('PLUGIN_PORT', '5555'))


def html_prod_to_dev(text):
    text = text.replace('https://askyourcode.ai', f'http://localhost:{PORT}')
    text = text.replace('https://plugin.askyourcode.ai', f'http://localhost:{PORT}')
    return text


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
    if DEVELOPMENT:
        text = html_prod_to_dev(text)
    return quart.Response(text, mimetype="text/json", status=200)


@app.get("/openapi.yaml")
async def openapi_spec():
    with open(OPENAPI_YAML_PATH, 'rt') as f:
        text = f.read()
    if DEVELOPMENT:
        text = html_prod_to_dev(text)
    return quart.Response(text, mimetype="text/yaml", status=200)


@app.post("/project/<string:username>")
async def download(username: str):
    if not username:
        return quart.Response(response='Missing username', status=400)

    body: Dict[str, str] = await quart.request.get_json(force=True)
    url: str = body.get('url')
    if not url:
        return quart.Response(response='Missing url', status=400)
    if not (url.startswith('http://') or url.startswith('https://')):
        return quart.Response(response='The URL must start with http:// or https://', status=400)
    if not DEVELOPMENT and ('://localhost' in url.lower() or '://127.' in url or '://192.168.' in url or '://10.' in url):
        return quart.Response(response='Invalid URL', status=400)

    # noinspection PyBroadException
    try:
        project_id = str(uuid.uuid4())
        print(f'Download project {project_id!r} for {username!r}')
        project = Project(username, project_id)
        await project.initialize(url)
    except KeyboardInterrupt:
        raise
    except ProjectException as e:
        print(f'ERROR: User: {username!r}; URL: {url!r}; Error: {e}')
        return quart.Response(response=str(e), status=400)

    if project_id.startswith('!'):
        response = {
            'error': project_id[1:]
        }
    else:
        response = {
            'project_id': project_id
        }

    return quart.Response(response=json.dumps(response, indent=2), status=200)


@app.delete("/project/<string:username>/<string:project_id>")
async def delete(username: str, project_id: str):
    if not username:
        return quart.Response(response='Missing username', status=400)

    print(f'Delete project {project_id!r} for {username!r}')
    project = Project(username, project_id)
    await project.delete()
    return quart.Response(response='OK', status=200)


@app.get("/project/<string:username>/<string:project_id>/search")
async def search(username: str, project_id: str):
    if not username:
        return quart.Response(response='ERROR: Missing username', status=400)

    text: str = request.args.get('text', '')

    try:
        limit = int(request.args.get('limit', '1'))
    except ValueError:
        limit = 1

    print(f'Search project {project_id!r} for {username!r} with limit {limit}: {text}')

    # noinspection PyBroadException
    try:
        project = Project(username, project_id)
        hits = await project.search(text, limit)
    except KeyboardInterrupt:
        raise
    except Exception:
        print(f'ERROR: User {username!r} failed to search project {project_id!r}:')
        print_exc()
        return quart.Response(response=f'Failed to search project {project_id!r}', status=400)

    results = [
        dict(
            score=hit.score,
            text=hit.fragment.text,
            path=hit.fragment.path,
            lineno=hit.fragment.lineno,
            name=hit.fragment.name,
        )
        for hit in hits
    ]

    return quart.Response(response=json.dumps(results, indent=2), status=200)


def main():
    app.run(debug=True, host="localhost", port=PORT)


async def run_task():
    await app.run_task(debug=True, host="localhost", port=PORT)


if __name__ == "__main__":
    main()

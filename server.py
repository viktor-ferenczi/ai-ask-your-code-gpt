import json
import sys
from traceback import print_exc
from typing import Dict

import quart
import quart_cors
from quart import request

import backend

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

_TODOS = {}

DEVELOPMENT = sys.platform == 'win32'


def html_prod_to_dev(text):
    text = text.replace('https://askyourcode.ai', 'http://127.0.0.1:5003')
    return text


@app.get("/")
async def index():
    return await quart.send_file('index.html', mimetype='text/html')


@app.get("/logo.png")
async def logo():
    return await quart.send_file('logo.png', mimetype='image/png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    with open("ai-plugin.json") as f:
        text = f.read()
    if DEVELOPMENT:
        text = html_prod_to_dev(text)
    return quart.Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    with open("openapi.yaml") as f:
        text = f.read()
    if DEVELOPMENT:
        text = html_prod_to_dev(text)
    return quart.Response(text, mimetype="text/yaml")


@app.post("/project/<string:username>")
async def download(username: str):
    if not username:
        return quart.Response(response='Missing username', status=400)

    body: Dict[str, str] = await quart.request.get_json(force=True)
    url: str = body.get('url')
    if not url:
        return quart.Response(response='Missing url')
    if not (url.startswith('http://') or url.startswith('https://')):
        return quart.Response(response='The URL must start with http:// or https://', status=400)

    # noinspection PyBroadException
    try:
        project_id = await backend.download(username, url)
    except KeyboardInterrupt:
        raise
    except Exception:
        print(f'ERROR: User {username!r} failed to download source archive {url!r}:')
        print_exc()
        return quart.Response(response='Failed to download or store the source archive', status=400)

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

    await backend.delete(username, project_id)
    return quart.Response(response='OK', status=200)


@app.get("/project/<string:username>/<string:project_id>/search")
async def search(username: str, project_id: str):
    if not username:
        return quart.Response(response='ERROR: Missing username', status=400)

    path: str = request.args.get('path', '')
    text: str = request.args.get('text', '')

    try:
        limit = int(request.args.get('limit', '1'))
    except ValueError:
        limit = 1

    # noinspection PyBroadException
    try:
        results = await backend.search(username, project_id, text, path, limit)
    except KeyboardInterrupt:
        raise
    except Exception:
        print(f'ERROR: User {username!r} failed to search project {project_id!r}:')
        print_exc()
        return quart.Response(response='ERROR: URL must start with http:// or https://', status=400)

    return quart.Response(response=json.dumps(results, indent=2), status=200)


def main():
    app.run(debug=True, host="127.0.0.1", port=5003)


if __name__ == "__main__":
    main()

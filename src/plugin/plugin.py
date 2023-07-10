import asyncio
import json
import os
import re
from traceback import print_exc
from typing import Dict, Optional, Union

import asyncpg
import quart
import quart_cors
from aiodebug import log_slow_callbacks
from asyncpg import Pool
from quart import request, Response

from common.constants import C
from common.http import check_url
from common.server import run_app
from common.tools import tiktoken_len, new_uuid
from logic.backend import Backend, BackendError
from storage import projects
from storage.database import Database

MODULE_DIR = os.path.dirname(__file__)
AI_PLUGIN_PATH = os.path.join(MODULE_DIR, 'ai-plugin.json')
OPENAPI_YAML_PATH = os.path.join(MODULE_DIR, 'openapi.yaml')


def modify_description_for_environment(text):
    if C.IS_PRODUCTION:
        return text

    text = text.replace('"AskYourCode"', f'"{C.PLUGIN_NAME}"')
    text = text.replace('"askyourcode"', f'"{C.PLUGIN_ID}"')
    text = text.replace('https://plugin.askyourcode.ai', C.PLUGIN_URL)
    return text


app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

DATABASE: Optional[Database] = None


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
    text = modify_description_for_environment(text)
    return Response(text, mimetype="text/json", status=200)


@app.get("/openapi.yaml")
async def openapi_spec():
    with open(OPENAPI_YAML_PATH, 'rt') as f:
        text = f.read()
    text = modify_description_for_environment(text)
    return Response(text, mimetype="text/yaml", status=200)


RX_GITHUB_REPO = re.compile(r'^https://github\.com/([^/]+)/([^/]+)/?$', re.I)
RX_GITHUB_CODELOAD = re.compile(r'^https://codeload\.github\.com/(.+?)/(.+?)/zip/refs/heads/(.+)$', re.I)

assert RX_GITHUB_REPO.match('https://github.com/Rapptz/discord.py/archive/refs/heads/master.zip') is None
assert RX_GITHUB_REPO.match('https://github.com/Rapptz/discord.py/').group(0) == 'https://github.com/Rapptz/discord.py/'
assert RX_GITHUB_REPO.match('https://github.com/Rapptz/discord.py').group(0) == 'https://github.com/Rapptz/discord.py'


@app.post("/project")
async def create():
    await ensure_database()

    body: Dict[str, str] = await quart.request.get_json(force=True)
    uid: str = ''  # FIXME: Get it from PluginLab
    url: str = body.get('url', '')

    # Validate the URL and apply workarounds as needed
    if url:
        response = await validate_url(url)
        if isinstance(response, Response):
            return response
        url = response

    project_name = url.split('?')[0]
    if len(project_name) > 60:
        project_name = new_uuid()

    # Create project, download and verify archive, initiate indexing
    print(f'Created project {project_name!r} from {url!r} for user {uid!r}')

    # noinspection PyBroadException
    try:
        backend = await Backend.ensure_project(DATABASE, uid, project_name)
        info = await backend.download(url) if url else dict(status='Created an empty project')
    except BackendError as e:
        return Response(response=f'{e}; Please find the FAQ, HowTo and bug-reports at askyourcode.ai', status=400)
    except Exception:
        print(f'ERROR: Failed to create project from archive URL {url!r}')
        print_exc()
        return Response(response='Failed to create project; Please find the FAQ, HowTo and bug-reports at askyourcode.ai', status=400)

    response = dict(project=project_name)
    if info:
        response['info'] = info

    return Response(response=json.dumps(response, indent=2), status=200)


# noinspection HttpUrlsUsage
async def validate_url(url: str) -> Union[str, Response]:
    original_url = url

    url = url.strip()
    if not (url.startswith('http://') or url.startswith('https://')):
        return Response(response='The URL must start with http:// or https://', status=400)

    # Common mistakes GPT-4 makes
    # https://github.com/yourusername/yourproject/
    # https://github.com/username/project/
    if '/yourusername/yourproject' in url or '/username/project' in url:
        return Response(response='Do not use an example URL directly', status=404)

    # Translate GitHub repo to ZIP download of main branch
    # FIXME: Auto-detect the default branch if possible (other than main and master)
    # FIXME: Detect private repos at the same time and direct the user to
    #        connect account to grant access or use another way to deliver
    #        the project files to the plugin (local agent)
    m = RX_GITHUB_REPO.match(url)
    if m is not None:
        url = f"{original_url.rstrip('/')}/archive/refs/heads/main.zip"
        if not await check_url(url):
            url = f"{original_url.rstrip('/')}/archive/refs/heads/master.zip"
            if not await check_url(url):
                return Response(response='Please point to the downloadable ZIP file of the repository branch you want to download', status=404)

    # Translate GitHub codeload URLs to normal ZIP download URLs. For example:
    # https://codeload.github.com/ShiZiqiang/dual-path-RNNs-DPRNNs-based-speech-separation/zip/refs/heads/master
    # =>
    # https://github.com/ShiZiqiang/dual-path-RNNs-DPRNNs-based-speech-separation/archive/refs/heads/master.zip
    m = RX_GITHUB_CODELOAD.match(url)
    if m is not None:
        url = f'https://github.com/{m.group(1)}/{m.group(2)}/archive/refs/heads/{m.group(3)}.zip'

    # Enable direct download from Dropbox
    if url.startswith('https://www.dropbox.com/') and url.endswith('?dl=0'):
        url = url[:-5] + '?dl=1'
    if url.startswith('https://www.dropbox.com/') and '?dl=0&' in url:
        url = url.replace('?dl=0&', '?dl=1&')

    # Cloud file sharing known not to work
    lc_url = url.lower()
    if 'https://drive.google.com/' in lc_url or 'https://1drv.ms/' in lc_url:
        return Response(response='Google Drive and OneDrive are not supported, Dropbox works. The URL must point to a publicly and directly downloadable ZIP file. Please use a GitHub ZIP download link or a direct file link from Discord. Please find the FAQ, HowTo and bug-reports at askyourcode.ai', status=400)

    # Protect against attacks
    if C.IS_PRODUCTION and ('://localhost' in lc_url or '://127.' in url or '://192.168.' in url or '://10.' in url):
        return Response(response='Invalid URL', status=400)

    return url


@app.get("/summarize")
async def summarize():
    await ensure_database()

    uid = ''
    project_name: str = request.args.get('project', '')

    path: str = request.args.get('path', '')
    tail: str = request.args.get('tail', '')
    name: str = request.args.get('name', '')

    print(f'Summarize project {project_name!r}: path={path!r}, tail={tail!r}, name={name!r}')

    if path == '.':
        path = '/'

    if not path.startswith('/'):
        path = f'/{path}'

    async with DATABASE.connection() as conn:
        project = await projects.find_by_uid_and_name(conn, uid, project_name)

    if project is None:
        return Response(response='No such project', status=404)

    backend = Backend(DATABASE, project)

    # noinspection PyBroadException
    try:
        text = await backend.summarize(path=path, tail=tail, name=name)
    except BackendError as e:
        print(f'Failed to summarize project {project_name!r}: {e}')
        print(f'- path={path!r}')
        print(f'- tail={tail!r}')
        print(f'- name={name!r}')
        return Response(response=str(e), status=400)
    except Exception:
        print(f'ERROR: Failed to summarize project {project_name!r}')
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

    # FIXME: Return information on indexing progress or hints if the search did not give any result
    info = None

    response = dict(summary=text)
    if info:
        response['info'] = info

    return Response(response=json.dumps(response, indent=2), status=200)


@app.get("/search")
async def search():
    await ensure_database()

    uid = ''
    project_name: str = request.args.get('project', '')

    path: str = request.args.get('path', '')
    tail: str = request.args.get('tail', '')
    name: str = request.args.get('name', '')
    text: str = request.args.get('text', '')

    limit: int = 1
    try:
        limit: int = int(request.args.get('limit', '1'))
    except ValueError:
        pass

    print(f'Search project {project_name!r}: path={path!r}, tail={tail!r}, name={name!r}, text={text!r}')

    if path == '.':
        path = '/'

    if not path.startswith('/'):
        path = f'/{path}'

    async with DATABASE.connection() as conn:
        project = await projects.find_by_uid_and_name(conn, uid, project_name)

    if project is None:
        return Response(response='No such project', status=404)

    backend = Backend(DATABASE, project)

    # noinspection PyBroadException
    try:
        hits = await backend.search(path=path, tail=tail, name=name, text=text, limit=limit)
        if not hits and name:
            hits = await backend.search(path=path, tail=tail, text=name, limit=limit)
            if not hits:
                hits = await backend.search(tail=tail, text=name, limit=limit)
            if not hits:
                hits = await backend.search(text=name, limit=10)
        if not hits and path:
            hits = await backend.search(tail='/' + path.rsplit('/')[-1], text=text, limit=limit)
    except BackendError as e:
        print(f'Failed to search project {project_name!r}: {e}')
        print(f'- path={path!r}')
        print(f'- tail={tail!r}')
        print(f'- name={name!r}')
        print(f'- text={text!r}')
        print(f'- limit={limit!r}')
        return Response(response=str(e), status=400)
    except Exception:
        print(f'ERROR: Failed to search project {project_name!r}')
        print(f'- path={path!r}')
        print(f'- tail={tail!r}')
        print(f'- name={name!r}')
        print(f'- text={text!r}')
        print(f'- limit={limit!r}')
        print_exc()
        return Response(response='Failed to search the project contents. Please try again later.', status=500)

    if not hits:
        return Response(response='No match found', status=204)

    # Shorten hits if needed
    max_tokens_per_hit = 2000 // limit
    for hit in hits:
        tokens = tiktoken_len(hit.text)
        if tiktoken_len(hit.text) > max_tokens_per_hit:
            hit.text = hit.text[:len(hit.text) * max_tokens_per_hit // tokens] + '...'

    results = [
        dict(
            path=hit.path,
            text=hit.text,
        )
        for hit in hits
    ]

    # FIXME: Return information on indexing progress
    info = {}
    if not hits:
        info['hint'] = 'Try again with a more relaxed search condition'

    response = dict(results=results)
    if info:
        response['info'] = info

    return Response(response=json.dumps(response, indent=2), status=200)


async def ensure_database():
    global DATABASE
    if DATABASE is not None:
        return

    # This happens only if run by hypercorn on server
    pool: Pool = asyncpg.create_pool(C.DATABASE_DSN, command_timeout=C.DATABASE_COMMAND_TIMEOUT, min_size=1, max_size=20)
    await pool._async__init__()
    DATABASE = Database(pool)
    # No cleanup is required, the process will just be terminated


async def main():
    global DATABASE
    async with Database.create_pool(C.DATABASE_DSN) as db:
        DATABASE = db
        try:
            await run_app(app, debug=C.DEVELOPMENT, host="localhost", port=C.PLUGIN_HTTP_PORT)
        finally:
            DATABASE = None


if __name__ == "__main__":
    log_slow_callbacks.enable(0.1)
    asyncio.run(main())

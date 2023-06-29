import asyncio
import os.path

from common.tools import tiktoken_len
from project.backend import Project

Project.dirname = 'test-projects'


async def main():
    project = Project('fe7c0fe0-e7b2-4fac-93e9-4283d85732bd')
    assert os.path.isfile(project.archive_path)
    assert os.path.isfile(project.db_path)

    summary = await project.summarize(path='/Plugins/FX/Niagara', tail='.h', token_limit=2000)
    print(f'Tokens: {tiktoken_len(summary)}')
    print(summary)


if __name__ == '__main__':
    asyncio.run(main())

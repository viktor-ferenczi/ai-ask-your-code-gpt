"""Deletes a project
"""
import asyncio
import sys

from project.backend import Project


async def main():
    project_id = sys.argv[1]
    project = Project(project_id)
    await project.cleanup()


if __name__ == '__main__':
    asyncio.run(main())

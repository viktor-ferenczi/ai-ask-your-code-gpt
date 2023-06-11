"""Deletes a project
"""
import asyncio
import sys
import time

from project.inventory import Inventory
from project.project import Project


async def main():
    hours = 24 if len(sys.argv) < 2 else int(sys.argv[1])
    assert hours >= 1
    cutoff = int(time.time()) - 3600 * hours

    inventory = Inventory()
    for project_id, url in inventory.get_expired_projects(cutoff=cutoff, limit=1):
        print(f'Removing: {project_id} ')
        project = Project(project_id)
        await project.cleanup()


if __name__ == '__main__':
    asyncio.run(main())

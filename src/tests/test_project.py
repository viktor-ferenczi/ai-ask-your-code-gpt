import asyncio
import os
import pprint
import shutil
import unittest
import zipfile
from typing import List

from quart import Quart, send_file

from common.constants import C
from downloader.downloader import app as downloader_app
from embed.embedder import app as embedder_app
from loader.loader import app as loader_app, workers as loader_workers
from model.hit import Hit
from project.inventory import Inventory
from project.project import Project

MODULE_DIR = os.path.dirname(__file__)


class TestProject(unittest.IsolatedAsyncioTestCase):
    test_project_dir = os.path.join(MODULE_DIR, '..', 'tests', 'TestProject')
    zip_path = os.path.join(MODULE_DIR, 'TestProject.zip')

    def setUp(self) -> None:
        self.maxDiff = 32768

        Inventory.filename = 'test-inventory.sqlite'
        inventory = Inventory()
        inventory.drop_database()

        Project.dirname = 'test-projects'
        test_projects_dir = os.path.join(C.DATA_DIR, Project.dirname)
        if os.path.isdir(test_projects_dir):
            shutil.rmtree(test_projects_dir)

        dir_len = len(self.test_project_dir) + 1
        with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.test_project_dir):
                for filename in files:
                    path = os.path.join(root, filename)
                    archive_path = path[dir_len:]
                    zipf.write(path, archive_path)

    def tearDown(self) -> None:
        try:
            os.remove(self.zip_path)
        except (IOError, OSError):
            pass

    async def serve_zip(self):
        self.app = Quart('test_zip_server')

        @self.app.route('/')
        async def serve_zip():
            return await send_file(self.zip_path, as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=49001)

    async def test_project(self):
        actual_test = asyncio.create_task(self.actual_test())
        zip_server_task = asyncio.create_task(self.serve_zip())
        query_embedder_task = asyncio.create_task(embedder_app.run_task(debug=True, host='localhost', port=40100))
        store_embedder_tasks = [asyncio.create_task(embedder_app.run_task(debug=True, host='localhost', port=40200 + i)) for i in (0, 1)]
        downloader_task = asyncio.create_task(downloader_app.run_task(debug=True, host='localhost', port=40001))
        loader_task = asyncio.create_task(loader_app.run_task(debug=True, host='localhost', port=40002))
        loader_worker_tasks = [asyncio.create_task(worker()) for worker in loader_workers]

        tasks = [actual_test, zip_server_task, query_embedder_task, downloader_task, loader_task] + store_embedder_tasks + loader_worker_tasks

        await asyncio.wait(tasks, timeout=3600.0, return_when=asyncio.FIRST_COMPLETED)

        actual_test.result()
        for task in tasks:
            if task is not actual_test:
                task.cancel()

    async def actual_test(self):
        await self.small_project()
        await self.medium_project()

    async def small_project(self):
        project_id = await Project.download('http://127.0.0.1:49001/')
        project = Project(project_id)

        await self.wait_for_processing(project)

        hits = await project.search(tail='.py', name='Duplicates')
        self.verify_hits(hits, 1, contains=['class Duplicates'])

        hits = await project.search(path='/find_duplicates.py', limit=10)
        self.verify_hits(hits, 7, path='/find_duplicates.py')

        hits = await project.search(tail='.py', path='/find_duplicates.py', limit=10)
        self.verify_hits(hits, 7, path='/find_duplicates.py')

        hits = await project.search(path='/README.md', limit=10)
        self.verify_hits(hits, 3, path='/README.md')

        # FIXME: Should be limit=1
        hits = await project.search(tail='.md', text='Lorem ipsum dolor sit amet, consectetur adipiscing elit.', limit=3)
        self.verify_hits(hits, 3, path='/README.md', contains=['Lorem ipsum dolor sit amet, consectetur adipiscing elit.'])

        summary = await project.summarize(tail='.md')
        self.assertEqual('''\
# Test project
## Rationale
### Doc types and languages
### Some long section
# End
''', summary)

        summary = await project.summarize(tail='.py')
        self.assertEqual('''\
Duplicates
Duplicates.__init__
Duplicates.collect
main
md5_checksum
''', summary)

        await project.delete()

    async def medium_project(self):
        project_id = await Project.download('https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip')
        project = Project(project_id)

        await self.wait_for_processing(project)

        hits = await project.search(path='/README.md', limit=10)
        self.verify_hits(hits, 3, path='/README.md')

        hits = await project.search(tail='.py', name='Query', limit=10)
        self.verify_hits(hits, 8, contains=['class Query'])

        summary = await project.summarize(tail='.md')
        self.assertEqual('''\
# Database Abstraction Layer Generator
# Installation
# How it works
## Abstraction layer
## Lightweight usage
## Features
# Remarks
## Performance
## Limitations
''', summary)

        summary = await project.summarize(tail='.py')
        self.assertEqual('''\
Activation
Add
AfterDeleteRow
AfterDeleteStatement
AfterInsertOrUpdateRow
AfterInsertOrUpdateStatement
AfterInsertRow
AfterInsertStatement
AfterUpdateRow
AfterUpdateStatement
And
Avg
BaseAggregate
BaseColumn
BaseColumnConstraint
BaseConstraint
BaseFunction
BaseIndex
BaseProcedure
BaseQueryResult
BaseTrigger
BeforeDeleteRow
BeforeDeleteStatement
BeforeInsertOrUpdateRow
BeforeInsertOrUpdateStatement
BeforeInsertRow
BeforeInsertStatement
BeforeUpdateRow
BeforeUpdateStatement
Boolean
Check
Clauses
Coalesce
ColumnInfo
Concat
Condition
Contains
Count
Custom
DataError
Database
DatabaseAbstraction
DatabaseError
DatabaseInspector
Date
Datetime
Decimal
Div
Equal
Error
Float
ForeignKey
FullTextSearch
FullTextSearchIndex
GMLExporter
GeneratorOptions
GreaterThan
GreaterThanOrEqual
Group
GroupRole
GroupUser
In
Index
Integer
IntegrityError
InterfaceError
InternalError
Invoice
InvoiceItem
Left
LessThan
LessThanOrEqual
Like
Match
Max
Min
Mul
NA
Neg
Not
NotEqual
NotIn
NotLike
NotMatch
NotSupportedError
OperationalError
Or
Payment
PostCondition
PrimaryKey
Procedure
Product
ProductSale
ProgrammingError
Query
Record
Result
Right
Role
SearchDocument
SlugMixin
Sub
Substring
Sum
Table
TestAbstraction
TestDatabaseModel
TestGraph
Text
Unique
User
UserContact
Var
Warning
format_add_function
format_and_function
format_avg_aggregate
format_boolean_column
format_check_constraint
format_coalesce_function
format_column
format_concat_function
format_constraint
format_contains_function
format_count_aggregate
format_create_btree_index
format_create_full_text_search_index
format_create_index
format_create_procedure
format_create_table
format_create_trigger
format_cross_join_group_list
format_custom_column
format_custom_function
format_date_column
format_datetime_column
format_decimal_column
format_default_not_null
format_delete
format_div_function
format_drop_btree_index
format_drop_full_text_search_index
format_drop_index
format_drop_procedure
format_drop_table
format_drop_trigger
format_eq_condition
format_equal_function
format_expression
format_float_column
format_foreign_key_column
format_foreign_key_constraint
format_full_text_search_function
format_function
format_ge_condition
format_greater_than_function
format_greater_than_or_equal_function
format_gt_condition
format_in_condition
format_in_function
format_insert
format_integer_column
format_le_condition
format_left_function
format_less_than_function
format_less_than_or_equal_function
format_like_condition
format_like_function
format_lt_condition
format_match_condition
format_match_function
format_max_aggregate
format_min_aggregate
format_mul_function
format_ne_condition
format_neg_function
format_not_equal_function
format_not_function
format_not_in_condition
format_not_in_function
format_not_in_range_condition
format_not_like_condition
format_not_like_function
format_not_match_condition
format_not_match_function
format_not_similar_to_condition
format_or_function
format_order_by
format_primary_key_column
format_primary_key_constraint
format_query
format_query_condition
format_query_condition_map
format_query_order_by_map
format_range_condition
format_release_savepoint
format_result
format_right_function
format_rollback_to_savepoint
format_savepoint
format_search_condition
format_search_document_column
format_select
format_similar_to_condition
format_sub_function
format_substring_function
format_sum_aggregate
format_table_column_condition
format_table_condition_map
format_table_order_by_map
format_text_column
format_truncate_table
format_truncate_table_list
format_unique_constraint
format_update
format_var_function
generate
get_next_definition_serial
get_random_id
log
quote_alias_name
quote_literal_value
quote_name
quote_table_column_name
replace_parameter_placeholders
''', summary)

        await project.delete()

    def verify_hits(self, hits: List[Hit], count: int, *, path: str = None, contains: List[str] = None):
        print(f'verify_hits(count={count!r}, path={path!r}, contains={contains!r})')

        try:
            self.assertEqual(count, len(hits))
            self.assertEqual(count, len(set(hit.uuid for hit in hits)))

            if path:
                for hit in hits:
                    self.assertEqual(path, hit.path)

                self.assertEqual(sorted(hits, key=lambda hit: (-hit.score, hit.path, hit.lineno)), hits)

            else:
                self.assertEqual(sorted(hits, key=lambda hit: (-hit.score, hit.uuid)), hits)

            if contains:
                for text in contains:
                    self.assertTrue(any((text in hit.text) for hit in hits))
        except AssertionError:
            print()
            print('hits = ')
            pprint.pprint(hits, width=120)
            print()
            raise

    async def wait_for_processing(self, project):
        inventory = Inventory()

        print('Waiting for extracting fragments...')
        while 1:
            if inventory.has_project_extracted(project.project_id):
                break
            await asyncio.sleep(0.2)
        print('Downloaded')

        print('Waiting for embedding fragments...')
        while 1:
            if inventory.has_project_embedded(project.project_id):
                break
            await asyncio.sleep(0.2)
        print('Embedded')

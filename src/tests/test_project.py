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
from loader.loader import app as loader_app, workers as loader_workers
from model.hit import Hit
from project.inventory import Inventory
from project.project import Project, ProjectError

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

    def test_download_server_not_running(self):
        def should_fail():
            asyncio.run(Project.download('http://127.0.0.1:57575/this-wont-exist'))

        self.assertRaises(ProjectError, should_fail)

    async def serve_zip(self):
        self.app = Quart('test_zip_server')

        @self.app.route('/test.zip')
        async def serve_zip():
            return await send_file(self.zip_path, as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=49001)

    async def test_project(self):
        actual_test = asyncio.create_task(self.actual_test())
        zip_server_task = asyncio.create_task(self.serve_zip())
        downloader_task = asyncio.create_task(downloader_app.run_task(debug=True, host='localhost', port=40001))
        loader_task = asyncio.create_task(loader_app.run_task(debug=True, host='localhost', port=40002))
        loader_worker_tasks = [asyncio.create_task(worker()) for worker in loader_workers]

        tasks = [actual_test, zip_server_task, downloader_task, loader_task] + loader_worker_tasks

        await asyncio.wait(tasks, timeout=999999.0, return_when=asyncio.FIRST_COMPLETED)

        actual_test.result()
        for task in tasks:
            if task is not actual_test:
                task.cancel()

    async def actual_test(self):
        await self.download_error()

        # project_id = await self.github_user_content()
        # project = Project(project_id)
        # self.assertTrue(project.exists)
        # await project.delete()
        # self.assertFalse(project.exists)

        small_project_id = await self.small_project()

        project = Project(small_project_id)
        self.assertTrue(project.exists)
        await project.cleanup()
        self.assertFalse(project.exists)

        medium_project_id_1 = await self.medium_project()
        self.assertNotEquals(small_project_id, medium_project_id_1)
        project = Project(medium_project_id_1)

        await self.medium_project(medium_project_id_1)

        await project.cleanup()
        self.assertFalse(project.exists)

        await self.medium_project(medium_project_id_1, False)

        await project.delete()
        self.assertFalse(project.exists)

        medium_project_id_2 = await self.medium_project()
        self.assertNotEquals(medium_project_id_1, medium_project_id_2)

        project = Project(medium_project_id_2)
        await project.delete()
        self.assertFalse(project.exists)

    async def download_error(self):
        try:
            await Project.download('http://127.0.0.1:49001/this-wont-exist')
        except ProjectError as e:
            self.assertTrue('Failed to download' in str(e))
        else:
            self.fail("ProjectError not raised")

    async def small_project(self) -> str:
        project_id = await Project.download('http://127.0.0.1:49001/test.zip')
        project = Project(project_id)

        await self.wait_for_processing(project)

        hits = await project.search(tail='.py', name='Duplicates')
        self.verify_hits(hits, 1, contains=['class Duplicates'])

        hits = await project.search(path='/find_duplicates.py', limit=100)
        self.verify_hits(hits, 34, path='/find_duplicates.py')

        hits = await project.search(tail='.py', path='/find_duplicates.py', limit=100)
        self.verify_hits(hits, 34, path='/find_duplicates.py')

        hits = await project.search(path='/README.md', limit=100)
        self.verify_hits(hits, 5, path='/README.md')

        hits = await project.search(tail='.md', text='standard set of source code files', limit=1)
        self.verify_hits(hits, 1, path='/README.md', contains=['standard set of source code files'])

        summary = await project.summarize(tail='.md')
        self.assertEqual('''\
File extensions: .md

# Markdown Syntax Examples
## Headings
# Heading 1
## Heading 2
### Heading 3
## Emphasis
## Lists
### Ordered List
### Unordered List
## Links
## Images
## Blockquotes
## Code

# Test project
## Rationale
### Doc types and languages
### Some long section
## Summary
''', summary)

        summary = await project.summarize(tail='.py')
        self.assertEqual('''\
File extensions: .py

Python: /find_duplicates.py
  Functions: main md5_checksum
  Classes: Duplicates
  Methods: __init__ collect
  Variables and usages: CHUNK_SIZE ProcessPoolExecutor append collections concurrent data defaultdict desc dirpath duplicates executor extend file_checksum file_checksums file_list file_path file_size filename filenames files files_by_checksum files_by_size first futures getsize hasher hashlib hexdigest input isdir items join open path pbar print read root_dir total total_size total_space_saved tqdm unit unit_scale update values walk
''', summary)

        return project_id

    async def medium_project(self, expect_project_id: str = '', expect_already_embedded: bool = True) -> str:
        project_id = await Project.download('https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip')
        project = Project(project_id)

        if expect_project_id:
            self.assertEqual(project_id, expect_project_id)

        if not expect_project_id or not expect_already_embedded:
            await self.wait_for_processing(project)

        progress = await project.get_progress()
        self.assertEqual(progress, 100)

        hits = await project.search(path='/README.md', limit=100)
        self.verify_hits(hits, 9, path='/README.md')

        hits = await project.search(tail='.py', name='Query', limit=100)
        self.verify_hits(hits, 34, contains=['class Query'])

        summary = await project.summarize(tail='.md')
        self.assertEqual('''\
File extensions: .md

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
File extensions: .py

Python: /lib/setup.py

Python: /lib/dblayer/constants.py
  Classes: NA
  Methods: __repr__

Python: /lib/dblayer/util.py
  Functions: get_next_definition_serial get_random_id log

Python: /lib/dblayer/generator/generator.py
  Functions: generate
  Classes: GeneratorOptions

Python: /lib/dblayer/graph/gml.py
  Classes: GMLExporter
  Methods: __init__ export

Python: /lib/dblayer/model/aggregate.py
  Classes: Avg BaseAggregate Count Max Min Sum
  Methods: __init__

Python: /lib/dblayer/model/column.py
  Classes: BaseColumn Boolean Custom Date Datetime Decimal Float ForeignKey Integer PrimaryKey SearchDocument Text
  Methods: __init__ __repr__ __str__ clone full_repr get_implicit_definition_list_for_table_class has_custom_default sort_key

Python: /lib/dblayer/model/constraint.py
  Classes: BaseColumnConstraint BaseConstraint Check ForeignKey PrimaryKey Unique
  Methods: __init__ __repr__ __str__ clone sort_key

Python: /lib/dblayer/model/database.py
  Classes: Database
  Methods: __init__ __new__ __repr__ __str__ generate initialize pretty_format_class

Python: /lib/dblayer/model/function.py
  Classes: Add And BaseFunction Coalesce Concat Contains Custom Div Equal FullTextSearch GreaterThan GreaterThanOrEqual In Left LessThan LessThanOrEqual Like Match Mul Neg Not NotEqual NotIn NotLike NotMatch Or Right Sub Substring Var
  Methods: __init__ __repr__ __str__

Python: /lib/dblayer/model/index.py
  Classes: BaseIndex FullTextSearchIndex Index
  Methods: __init__ __repr__ __str__ clone get_implicit_definition_list_for_table_class sort_key

Python: /lib/dblayer/model/procedure.py
  Classes: BaseProcedure Procedure
  Methods: __init__ __repr__ __str__ clone sort_key

Python: /lib/dblayer/model/query.py
  Classes: BaseQueryResult Condition PostCondition Query Result
  Methods: __init__ __new__ __repr__ _collect_result_condition_list clone get_table_list initialize iterate_joined_tables pretty_format_class

Python: /lib/dblayer/model/table.py
  Classes: Table
  Methods: __init__ __new__ __repr__ _prepare_table_definition _sort_key initialize join pretty_format_class

Python: /lib/dblayer/model/trigger.py
  Classes: AfterDeleteRow AfterDeleteStatement AfterInsertOrUpdateRow AfterInsertOrUpdateStatement AfterInsertRow AfterInsertStatement AfterUpdateRow AfterUpdateStatement BaseTrigger BeforeDeleteRow BeforeDeleteStatement BeforeInsertOrUpdateRow BeforeInsertOrUpdateStatement BeforeInsertRow BeforeInsertStatement BeforeUpdateRow BeforeUpdateStatement
  Methods: __init__ __repr__ __str__ clone sort_key

Python: /lib/dblayer/test/constants.py

Python: /lib/dblayer/test/model.py
  Functions: generate
  Classes: Activation Group GroupRole GroupUser Invoice InvoiceItem Payment Product ProductSale Role SlugMixin TestDatabaseModel User UserContact

Python: /lib/dblayer/test/test_abstraction.py
  Classes: TestAbstraction TestGraph
  Methods: do_failed_transaction load_data modify_data setUp tearDown testGML test_class_formatting test_clauses_class test_database_session test_duplicate_insert test_full_text_search test_insert_select test_inspection test_order_by test_product_sale_query test_random_id_selection test_repr_str test_triggers test_truncate test_tuple_dict test_update_delete test_user_contact_query verify_data

Python: /lib/dblayer/backend/base/clauses.py
  Classes: Clauses
  Methods: __eq__ __hash__ __init__ __repr__ get_tuple

Python: /lib/dblayer/backend/base/database.py
  Classes: DatabaseAbstraction
  Methods: __del__ _connect add_record add_record_list close commit connect connected create_language cursor delete_record delete_record_list disable_transactions enable_transactions execute execute_and_fetch_dict_iter execute_and_fetch_iter execute_and_fetch_one execute_statement_list executemany get_last_value_of_last_sequence_used get_record get_record_iter get_record_list is_primary_key_conflict log_analysis rollback session transaction update_record update_record_list

Python: /lib/dblayer/backend/base/error.py
  Classes: DataError DatabaseError Error IntegrityError InterfaceError InternalError NotSupportedError OperationalError ProgrammingError Warning

Python: /lib/dblayer/backend/base/format.py
  Functions: format_add_function format_and_function format_avg_aggregate format_boolean_column format_check_constraint format_coalesce_function format_column format_concat_function format_constraint format_contains_function format_count_aggregate format_create_btree_index format_create_full_text_search_index format_create_index format_create_procedure format_create_table format_create_trigger format_cross_join_group_list format_custom_column format_custom_function format_date_column format_datetime_column format_decimal_column format_default_not_null format_delete format_div_function format_drop_btree_index format_drop_full_text_search_index format_drop_index format_drop_procedure format_drop_table format_drop_trigger format_eq_condition format_equal_function format_expression format_float_column format_foreign_key_column format_foreign_key_constraint format_full_text_search_function format_function format_ge_condition format_greater_than_function format_greater_than_or_equal_function format_gt_condition format_in_condition format_in_function format_insert format_integer_column format_le_condition format_left_function format_less_than_function format_less_than_or_equal_function format_like_condition format_like_function format_lt_condition format_match_condition format_match_function format_max_aggregate format_min_aggregate format_mul_function format_ne_condition format_neg_function format_not_equal_function format_not_function format_not_in_condition format_not_in_function format_not_in_range_condition format_not_like_condition format_not_like_function format_not_match_condition format_not_match_function format_not_similar_to_condition format_or_function format_order_by format_primary_key_column format_primary_key_constraint format_query format_query_condition format_query_condition_map format_query_order_by_map format_range_condition format_release_savepoint format_result format_right_function format_rollback_to_savepoint format_savepoint format_search_condition format_search_document_column format_select format_similar_to_condition format_sub_function format_substring_function format_sum_aggregate format_table_column_condition format_table_condition_map format_table_order_by_map format_text_column format_truncate_table format_truncate_table_list format_unique_constraint format_update format_var_function quote_alias_name quote_literal_value quote_name quote_table_column_name replace_parameter_placeholders

Python: /lib/dblayer/backend/base/record.py
  Classes: Record
  Methods: __eq__ __repr__ finalize

Python: /lib/dblayer/backend/postgresql/clauses.py

Python: /lib/dblayer/backend/postgresql/database.py
  Classes: DatabaseAbstraction
  Methods: _connect

Python: /lib/dblayer/backend/postgresql/error.py

Python: /lib/dblayer/backend/postgresql/format.py

Python: /lib/dblayer/backend/postgresql/inspector.py
  Classes: ColumnInfo DatabaseInspector
  Methods: __init__ __repr__ convert_table_name_to_python define_bigint_column define_boolean_column define_custom_column define_date_column define_double_column define_integer_column define_numeric_column define_primary_key_column define_real_column define_text_column define_timestamp_column define_tsvector_column define_varchar_column inspect inspect_tables load_information_schema

Python: /lib/dblayer/backend/postgresql/record.py
''', summary)

        return project.project_id

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

    # async def github_user_content(self) -> str:
    #     url = 'https://raw.githubusercontent.com/manbearwiz/youtube-dl-server/main/youtube-dl-server.py'
    #     project_id = await Project.download(url)
    #     project = Project(project_id)
    #
    #     await self.wait_for_processing(project)
    #
    #     hits = await project.search(tail='.py')
    #     self.assertTrue(len(hits) > 0)
    #
    #     return project_id

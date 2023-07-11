from base_database_test import BaseDatabaseTest
from logic.backend import Backend, TInfo


# class TestDownloadServerNotRunning(BaseDatabaseTest):
#     test_script = __file__
#
#     async def test_download_server_not_running(self):
#         backend = await Backend.ensure_project(self.db, 'tester', 'test_download_server_not_running')
#         info: TInfo = await backend.download('http://127.0.0.1:57575', timeout=1.0)
#         print(info)
#         self.assertTrue('The download is still in progress' in info['status'])
#         self.assertTrue('hint' in info)

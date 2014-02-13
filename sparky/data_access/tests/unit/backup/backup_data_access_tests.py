import unittest
from sparky.data_access.backup.BackupDataAccess import BackupDataAccess
from sparky.data_access.tests.common.MockDataStore import MockDataStore

class BackupDataAccessTests(unittest.TestCase):
    def test_get_completed_backup_report_found(self):
        ds = MockDataStore()
        bds = BackupDataAccess(ds)
        result = bds.get_completed_backup_report(989)
        self.assertEqual(result['id'], '989')

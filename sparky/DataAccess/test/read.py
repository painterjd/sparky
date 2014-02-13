from sparky.DataAccess.Backup.BackupDataAccess import backup_data_access
from mock_data_store import mock_data_store

ds = mock_data_store()
bds = backup_data_access(ds)
print bds.get_completed_backup_report(989)

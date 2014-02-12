class BackupDataAccess(object):
    def __init__(self, data_store):
        self.data_store = data_store
        pass

    def GetCompletedBackups(self, backup_configuration_id):
        """

        """
        return self.data_store.GetData('EXEC spGetReportForBackup @backupId='+str(backup_configuration_id))

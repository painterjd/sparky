class backup_data_access(object):
    def __init__(self, data_store):
        self.data_store = data_store
        pass

    def get_completed_backup_report(self, backup_configuration_id):
        """

        """
        return self.data_store.get_data('EXEC spGetReportForBackup %d', backup_configuration_id)

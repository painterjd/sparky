from getpass import getpass
from sparky.DataAccess.Backup.BackupDataAccess import BackupDataAccess
from sparky.DataAccess.common.data_store import DataStore
from sqlalchemy.engine.url import make_url

user = raw_input('Username: ')
password = getpass()
print(" ")
server = raw_input('Server: ')
port = raw_input('Port: ')
database = raw_input('Database: ')

url = make_url('mssql+pymssql://' +
                user+':'+password +
                '@' + server + ':' + port +
                '/' + database)

ds = DataStore(url)
bda = BackupDataAccess(ds)
print bda.GetCompletedBackups(989)
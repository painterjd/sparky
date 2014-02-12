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

connect_string = 'mssql+pymssql://'
connect_string = connect_string + user
connect_string = connect_string + ':'
connect_string = connect_string + password
connect_string = connect_string + '@'
connect_string = connect_string + server
connect_string = connect_string + ':'
connect_string = connect_string + port
connect_string = connect_string + '/'
connect_string = connect_string + database

ds = DataStore(make_url(connect_string))
bda = BackupDataAccess(ds)
print bda.GetCompletedBackups(989)
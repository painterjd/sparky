import datetime
from sqlalchemy import create_engine

backups_completed = {'989': {'id': 592, 
    'backup_ id':989, 
    'backup_ configuration_id':1, 
    'backup_ configuration_name':u'Backup to a backup to a backup',  
    'is_ deleted':False,  
    'source_ machine_agent_id':1,  
    'source_ domain_username_id':1,  
    'source_ machine_name':u'THELONEINDIAN',  
    'source_ agent_version':u'0',  
    'source_ agent_key':u'aVRhclZUc2xkcFFsaUo1NGlTTk1kNEoyYmZ6T0h2eU1CYWVrVmRndFQ0cEdTL1gvUU1UNmJjeUlOUEh3NWhzVmpRaHZSQ2JIZkZrTHFTam1XSU9pdzBGcGNrWnZjbU5sVDI1bA==',  
    'source_ vault_guid':u'470070af-61ee-44b1-af58-a0a5079aa986',  
    'source_ architecture':u'64-bit',  
    'source_ OS':u'Windows 7',  
    'source_ OS_version':u'6.1',  
    'source_ ipaddress':None,  
    'source_ public_key_mod':u'B835EAE51F838F659FA9546766B3F81CA28660F3A07A990DF66ED38044FF36EC41EDCB4709BFFB2B995F0365A37F93E9FF6BBA11D9D40EA13351CB3E9F3082EC1E842B79627940D21A0B19EA0AB54B5C3CADE4E346672DCB7CD952BC9908CD7781C8A48E3F2650BEC6BE50B2704EA49F07F08C37DF07C33793FFE03A4AEC94DBC62577031BB3932D5C95AA7A983752B86F0B17D6E9E8FE341F479A890153FF234ECCA1F05E64C13D194BB965FD5C1638AD2A206F334CC222F268D960CE55232BE3279F75E832E9E8D20328E6DC37DD5F1A981F7D2453B7BD77E206381CD2A1B107975D032A9EA22F84151E0A5CF67CBF28840C97C19414FCE78E8F3CA36BC29F',  
    'source_ public_key_exp':10001,  
    'source_ is_encrypted':True,  
    'source_ is_disabled':False,  
    'source_ is_deleted':False,  
    'source_ is_data_deleted':True,  
    'source_ use_servicenet':False,  
    'source_ failover_enabled':False,  
    'source_ date_disabled':None,  
    'source_ date_deleted':datetime.datetime(2012, 2, 21, 0, 0),  
    'source_ flavor_id':3,  
    'source_ datacenter':None,  
    'source_ LUB':u'2014-01-10 1:00:00',  
    'source_ LUD':datetime.datetime(2014, 1, 10, 21, 51, 18, 243000),  
    'source_ container_name':u'CloudBackup_v2_0_470070af-61ee-44b1-af58-a0a5079aa986',  
    'source_ storage_provider':None,  
    'source_ storage_location':None,  
    'source_ storage_location_base_url':None,  
    'source_ hostserver_id':u'427df52d-1fd2-4f85-a132-79746ea1f6cc',  
    'source_ hostserver_host_guid':None,  
    'source_ hostserver_ipaddresses':None,  
    'source_ hostserver_type':1,  
    'source_ project_id':u'355452',  
    'current_ state':u'Completed',  
    'is_ purged':True,  
    'started_ time':datetime.datetime(2011, 10, 26, 16, 4, 20),  
    'ended_ time':datetime.datetime(2011, 10, 26, 16, 4, 24),  
    'files_ searched':0L,  
    'bytes_ searched':0L,  
    'files_ backedup':0L,  
    'bytes_ backedup':0L,  
    'total_ errors':0L,  
    'reason': u'No errors',  
    'diagnostics': None,  
    'snapshot_ id':1
    }}

def mock_get_backups_completed(id):
    print id
    print type(id)
    return backups_completed[id]

mock_dict = {'spGetReportForBackup': mock_get_backups_completed}
   
def mocker(sql, *multiparams, **params):
   """
   Assuming format like:
   EXEC spSomeProc @parm1=val1,  @parm2=val2, ...
   """

   tokens = sql[0].format(sql[1]).split(' ')
   try:
      return mock_dict[tokens[1]](tokens[2])
   except KeyError:
      print(tokens[1]+" is not a known procedure.")

# TODO: inherit data_store and pass create_machine parameters to specify mock strategy
class mock_data_store(object):
    def __init__(self):
        self.engine = create_engine('mssql+pymssql://', strategy='mock', executor=mocker)

    def get_data(self, *args, **kwargs):
        # This isn't exactly like the data_store implementation because this engine isn't returning a resultproxy
         return self.engine.execute(args, kwargs)

from sqlalchemy import create_engine

class DataStore(object):
    """

    """
    def __init__(self, connect_string):
        self.connect_string = connect_string
        self.engine = create_engine(connect_string)


    def GetData(self, cmd):
         return [value for value in self.engine.execute(cmd)]

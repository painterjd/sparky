from sqlalchemy import create_engine

class data_store(object):
    """

    """
    def __init__(self, connect_string):
        self.connect_string = connect_string
        self.engine = create_engine(connect_string)


    def get_data(self, cmd):
         return self.engine.execute(cmd).fetchone()

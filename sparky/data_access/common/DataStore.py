from sqlalchemy import create_engine
import abc
import six

@six.add_metaclass(abc.ABCMeta)
class DataStore(object):
    """
    """
    def __init__(self, *args, **kwargs):
        self.engine = create_engine(args, *kwargs)

    def get_data(self, cmd):
         return self.engine.execute(cmd).fetchone()

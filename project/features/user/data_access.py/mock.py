
from .abstraction import AbstractionDataAccess

class MockDataAccess(AbstractionDataAccess):
     def __init__(self,data_access):
         self.data_access=data_access
     def create_user(self,first_name,last_name):
        pass
     def get_user_by_id(self,user_id):
        pass

from .abstraction import AbstractionDataAccess

class MockDataAccess(AbstractionDataAccess):
     def __init__(self,data_access):
         self.data_access=data_access
     def create_user(self,first_name,last_name):
        pass
     def get_user_by_id(self,user_id):
        pass
     def update_token_user_id(self,token_id,user_id):
        pass
     def delete_user(self,user_id):
         pass
        
     def is_token_in_use(self,token_id):
         pass
        
from .abstraction import AbstractionUserService
from ..exceptions import FailedToCreateUser,UserNotExist,AccountAlreadyCreated
import logging
class DefaultUserService(AbstractionUserService):

    def __init__(self,data_access):
        self.data_access=data_access

    def create_user(self, first_name, last_name, token_id):
     if self.data_access.is_token_in_use(token_id):
        raise AccountAlreadyCreated
    
     user_created = self.data_access.create_user(first_name, last_name)
     if not user_created:
        raise FailedToCreateUser
    
     success = self.data_access.update_token_user_id(token_id, user_created.id)
     if not success:
        raise FailedToCreateUser
     return user_created


    def get_user_by_id(self,user_id):
        get_user=self.data_access.get_user_by_id(user_id)
        if not get_user:
            raise UserNotExist(user_id=user_id)
        return get_user
    def delete_user(self,user_id):
       delete_user=self.data_access.delete_user(user_id)
       if not delete_user:
          raise UserNotExist(user_id=user_id)
       return delete_user
       
        



       
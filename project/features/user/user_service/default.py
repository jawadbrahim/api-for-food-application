from .abstraction import AbstractionUserService
from ..exceptions import FailedToCreateUser,UserNotExist
class DefaultUserService(AbstractionUserService):

    def __init__(self,data_access):
        self.data_access=data_access

    def create_user(self,first_name,last_name):

        user_created=self.data_access.create_user(first_name,last_name)
        if not user_created:
            raise FailedToCreateUser
        return user_created
    def get_user_by_id(self,user_id):
        get_user=self.data_access.get_user_by_id(user_id)
        if not get_user:
            raise UserNotExist
        return get_user
        



       
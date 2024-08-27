import abc

class AbstractionDataAccess(metaclass=abc.ABCMeta):
    def create_user(self):
        raise NotImplementedError()
    def get_user_by_id(self):
        raise NotImplementedError()
    def delete_user(self):
        raise NotImplementedError()
    def is_token_in_use(self):
        raise NotImplementedError()
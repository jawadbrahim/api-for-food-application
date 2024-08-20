import abc

class AbstractionDataAccess(metaclass=abc.ABCMeta):

    def create_account(self):
        raise NotImplementedError()
    def get_account(self):
        raise NotImplementedError()
    def update_account(self):
        raise NotImplementedError()
    def update_token(self):
        raise NotImplementedError()
    def delete_account(self):
        raise NotImplementedError()
    def verify_password(self):
        raise NotImplementedError()
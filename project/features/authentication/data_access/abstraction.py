import abc

class AbstractionDataAccess(metaclass=abc.ABCMeta):

    def create_account(self):
        raise NotImplementedError()
    def email_exists(self):
        raise NotImplementedError()
    def email_password_exists(self):
        raise NotImplementedError()
    def get_account(self):
        raise NotImplementedError()
    def insert_token(self):
        raise NotImplementedError()
    def delete_account(self):
        raise NotImplementedError()
   
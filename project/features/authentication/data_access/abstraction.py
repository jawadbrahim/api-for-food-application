import abc

class AbstractionDataAccess(metaclass=abc.ABCMeta):

    def get_email(self):
        raise NotImplementedError()
    def get_email_password(self):
        raise NotImplementedError()
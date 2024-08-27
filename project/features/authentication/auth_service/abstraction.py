import abc

class AbstractionAuthService(metaclass=abc.ABCMeta):
    def register(self):
        raise NotImplementedError()
    def login(self):
        raise NotImplementedError()
    def get_account(self):
        raise NotImplementedError()
    def delete_account(self):
        raise NotImplementedError()
    
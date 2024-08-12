import abc

class AbstractionUserService(metaclass=abc.ABCMeta):
    def create_user(self):
        raise NotImplementedError()
    def get_user_by_id(self):
        raise NotImplementedError()
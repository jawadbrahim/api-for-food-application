import abc

class AbstractionRequestvalidator(metaclass=abc.ABCMeta):
    def validate_register(self):
        raise NotImplementedError()
    def validate_login(self):
        raise NotImplementedError()
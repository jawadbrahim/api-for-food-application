import abc

class AbstractionRequestValidator(metaclass=abc.ABCMeta):
    def valdiate_create_user(self):
        raise NotImplementedError()
    
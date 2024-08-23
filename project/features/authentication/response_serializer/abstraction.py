import abc

class AbstractionResponseSerializer(metaclass=abc.ABCMeta):
    def serialize_register(self):
        raise NotImplementedError()
    def serialize_delete_account(self):
        raise NotImplementedError()

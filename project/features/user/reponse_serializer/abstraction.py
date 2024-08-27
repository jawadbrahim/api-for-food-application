import abc

class AbstractionReponseSerializer(metaclass=abc.ABCMeta):
    def serialize_create_user(self):
        raise NotImplementedError()
    def serialize_delete_user(self):
        raise NotImplementedError()
        
import abc

class AbstractionReponseSerializer(metaclass=abc.ABCMeta):
    def serialize_create_user(self):
        raise NotImplementedError()
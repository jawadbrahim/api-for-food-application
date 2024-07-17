import abc 

class AbstractionReponseSerializer(metaclass=abc.ABCMeta):

    def serialize_create_food(self):
        raise NotImplementedError()
    def serialize_update_food(self):
        raise NotImplementedError()
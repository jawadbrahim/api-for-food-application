import abc

class AbstractionRequestvalidator(metaclass=abc.ABCMeta):
    def validate_create_food(self):
        raise NotImplementedError()
    def validate_update_foods(self):
        raise NotImplementedError()

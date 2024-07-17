import abc

class AbstractionFoodService(metaclass=abc.ABCMeta):
    def create_food(self):
        raise NotImplementedError()
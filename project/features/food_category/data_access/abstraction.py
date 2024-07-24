import abc

class AbstractionDataAccess(metaclass=abc.ABCMeta):

    def create_foods(self):
        raise NotImplementedError()
    def get_food_by_id(self):
        raise NotImplementedError()
    def get_food_by_group(self):
        raise NotImplementedError()
    def update_food(self):
        raise NotImplementedError()
    def delete_food(self):
        raise NotImplementedError()
    def search_food(self):
        raise NotImplementedError()
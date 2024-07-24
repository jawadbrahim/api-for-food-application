from .abstraction import AbstractionFoodService

class MockFoodService(AbstractionFoodService):
    def __init__(self, data_access):
      #   self.data_access = data_access
      pass  
    def create_food(self, category, title, description, picture, ingredients):
      #   return self.data_access.create_food(category, title, description, picture, ingredients)
         pass
    def get_foods_by_id(self, food_id):
      #   return self.data_access.get_food_by_id(food_id)
         pass
    def get_food_by_group(self):
      #   return self.data_access.get_food_by_group()
         pass
    def update_food(self, food_id, category, title, description, picture, ingredients):
      #   return self.data_access.update_food(food_id, category, title, description, picture, ingredients)
         pass
    def delete_food(self, food_id):
      #   return self.data_access.delete_food(food_id)
         pass
    def search_food(self, title):
      #   return self.data_access.search_food(title)
         pass
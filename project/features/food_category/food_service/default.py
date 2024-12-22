from .abstraction import AbstractionFoodService
from ..exceptions import FoodFailedToCreate,FoodNotExist,GroupedFoodIsEmpty,TitleNotFound,UserNotExist
class DefaultFoodService(AbstractionFoodService):
    #DI
    def __init__(self, data_access):
        self.data_access = data_access

    def create_foods(self, category, title, description, picture, ingredients):
        created = self.data_access.create_food(category, title, description, picture, ingredients)
        if not created:
            raise FoodFailedToCreate
        return created
        
           
    def get_foods_by_id(self,food_id):
        food= self.data_access.get_food_by_id(food_id)
        if not food :
            raise FoodNotExist(food_id=food_id)
        return food
    
    def get_food_by_group(self,page=1,per_page=10):
        grouped_food=self.data_access.get_food_by_group(page,per_page)
        if not grouped_food:
            raise GroupedFoodIsEmpty
        return grouped_food
    
    def update_food(self, food_id, category, title, description, picture, ingredients):
        updated_food = self.data_access.update_food(food_id, category, title, description, picture, ingredients)
        if not updated_food:
            raise FoodNotExist(food_id=food_id)
        return updated_food
    
    def delete_food(self,food_id):
        deleted_food=self.data_access.delete_food(food_id)
        if not deleted_food:
            raise FoodNotExist(food_id=food_id)
        return deleted_food
    
    def search_food(self,title):
        search_foods=self.data_access.search_food(title)
        if not search_foods:
             raise TitleNotFound(title=title)
        return search_foods
    def add_favorite_food(self, user_id, food_id):
      food = self.data_access.get_food_by_id(food_id)
      if not food:
            raise FoodNotExist(food_id=food_id)
        
      favorite = self.data_access.add_favorite_food(user_id, food_id)
      return favorite
    
    def get_favorite_foods_by_user(self, user_id):
        favorite_foods = self.data_access.get_favorite_foods_by_user(user_id)
        if not favorite_foods:
            raise UserNotExist(user_id=user_id)
        return favorite_foods

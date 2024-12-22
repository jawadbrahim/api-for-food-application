from .abstraction import AbstractionDataAccess
from project.model.food_category import Foods
from project.model.favorites import Favorite
from project.module.ormsqlachemy import OrmSqlalchemy

import json

class OrmSqlalchemyFoodCategory(AbstractionDataAccess,OrmSqlalchemy):

 def create_food(self, category, title, description, picture, ingredients):
        food = Foods(
            category=category,
            title=title,
            description=description,
            picture=picture,
            ingredients=ingredients,
        )
        self.add(food)
        return food
 def get_food_by_id(self, food_id):
    food = Foods.query.filter(Foods.id == food_id).first()
    if food:
        food_data = {
            "id": food.id,
            "category": food.category,
            "title": food.title,
            "description": food.description,
            "picture": food.picture,
            "ingredients": food.ingredients
        }
        return json.dumps(food_data,ensure_ascii=False)
    return None

 
 def get_food_by_group(self, page=1, per_page=10):
    foods = Foods.query.paginate(page=page, per_page=per_page, error_out=False)
    
    grouped_food = {}
    for food in foods.items:
        category = food.category
        if category not in grouped_food:
            grouped_food[category] = []
        food_data = {
            "title": food.title,
            "description": food.description,
            "picture": food.picture,
            "ingredients": food.ingredients
        }
        grouped_food[category].append(food_data)
    
    result={
        "food": grouped_food,
        "total": foods.total,
        "page": foods.page,
        "pages": foods.pages
    }
    return json.dumps(result,ensure_ascii=False)

 def update_food(self, food_id, category, title, description, picture, ingredients):
        food = Foods.query.filter_by(id=food_id).first()
        if food:
            food.category = category
            food.title = title
            food.description = description
            food.picture = picture
            food.ingredients = ingredients
            return food 
        else:
            return None
 def delete_food(self, food_id):
        food = Foods.q.filter(Foods.id == food_id).first()
        if food:
            self.delete(food)
        return food
           
        
 def search_food(self, title):
    search = Foods.query.filter(Foods.title.ilike(f"%{title}%")).all()
    if search:
        search_results = [
            {
                "id": food.id,
                "category": food.category,
                "title": food.title,
                "description": food.description,
                "picture": food.picture,
                "ingredients": food.ingredients
            }
            for food in search
        ]
        return search_results
 def add_favorite_food(self, user_id, food_id):
        favorite = Favorite(user_id=user_id, food_id=food_id)
        self.add_and_flush(favorite)
        return favorite
    
 def  get_favorite_foods_by_user (self, user_id):
        favorites = Favorite.query.filter_by(user_id=user_id).all()
        favorite_foods = [
            {
                "food_id": fav.food_id,
                "title": fav.food.title,
                "category": fav.food.category,
                "description": fav.food.description,
                "picture": fav.food.picture
            }
            for fav in favorites
        ]
        return favorite_foods
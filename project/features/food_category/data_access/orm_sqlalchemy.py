from .abstraction import AbstractionDataAccess
from project.model.food_category import Foods
from database.postgres import db
from project.module.ormsqlachemy import OrmSqlalchemy



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
        return food_data
    

 
 def get_food_by_group(self):
     foods=Foods.query.all()
     
     grouped_food={}
     
     for food in foods:
        category=food.category
        if category not in grouped_food:
              grouped_food[category]=[]
        food_data={
         
            "title":food.title,
            "description":food.description,
            "picture":food.picture,
            "ingredients":food.ingredients


     }
    
    
        grouped_food[category].append(food_data)
     return grouped_food
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
        food = Foods.query.filter(Foods.id == food_id).first()
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
from .abstraction import AbstractionDataAccess
from project.model.food_category import Foods
from database.postgres import db
from datetime import datetime
from ....cache.redis_cache import set_cache,get_cache


class OrmSqlalchemyFoodCategory(AbstractionDataAccess):

 def create_food(self, category, title, description, picture, ingredients):
        food = Foods(
            category=category,
            title=title,
            description=description,
            picture=picture,
            ingredients=ingredients,
        )
        db.session.add(food)
        db.session.flush()
        db.session.commit()
        return food
 def get_food_by_id(self, food_id):
    # cache_key = f"food:{food_id}"
    # cached_data = get_cache(cache_key)
    # if cached_data:
        # return json.loads(cached_data)
    
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
        # set_cache(cache_key, food_data)
        return food_data
    

 
 def get_food_by_group(self):
    #  cache_key="food:gruped"
    #  cache_date=get_cache(cache_key)
    #  if cache_date:
        #   return json.loads(cache_date)
     
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
        # set_cache(cache_key,grouped_food)
     return grouped_food
 def update_food(self, food_id, category, title, description, picture, ingredients):
        food = Foods.query.filter_by(id=food_id).first()
        if food:
            food.category = category
            food.title = title
            food.description = description
            food.picture = picture
            food.ingredients = ingredients
            food.updated_at =  datetime.utcnow()
            db.session.commit()
            return food 
        else:
            return None
 def delete_food(self, food_id):
        food = Foods.query.filter(Foods.id == food_id).first()
        if food:
            db.session.delete(food)
            db.session.commit()
        return food
           
        
 def search_food(self, title):
    # cache_key = f"food:search:{title}"
    # cached_data = get_cache(cache_key)
    # if cached_data:
        # return json.loads(cached_data)
    
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
        # set_cache(cache_key, search_results)
        return search_results
    
                
            
    


        
     
 
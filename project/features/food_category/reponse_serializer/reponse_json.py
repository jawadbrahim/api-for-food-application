from .abstraction import AbstractionReponseSerializer
from .reponse_serializer_models import ModelReponse_serialize, FoodUpdateSerializer,DeletedFoodSerializer,FavoriteSerializer
from project.features.food_category.data_classes import FoodDataclasses, FoodUpdatedDataClasses,FoodDeletedDataClasse,FavoriteDataClass

class Reponse_json(AbstractionReponseSerializer):
    def serialize_create_food(self, food):
            food=FoodDataclasses (
            id=food.id,
            category=food.category,
            title=food.title,
            description=food.description,
            picture=food.picture,
            ingredients=food.ingredients
            )
            response=ModelReponse_serialize(food=food)
            return response.json()

    def serialize_update_food(self, updated_food):
        updated_foods = FoodUpdatedDataClasses(
        
            category=updated_food.category,
            title=updated_food.title,
            description=updated_food.description,
            picture=updated_food.picture,
            ingredients=updated_food.ingredients
            )
        
        response = FoodUpdateSerializer(updated_food=updated_foods)
        return response.json()
    def serialize_delete_food(self, food):
        food_data = FoodDeletedDataClasse(
            id=food.id
        )
        response = DeletedFoodSerializer(food=food_data)
        return response.json()
    def serialize_favorite_created(self, favorite):
     favorite_data = FavoriteDataClass(
        user_id=favorite.user_id,
        food_id=favorite.food_id,
        created_at=favorite.created_at
    )
     response = FavoriteSerializer(favorite=favorite_data)
     return response.json()

              
         
         
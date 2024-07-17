from .abstraction import AbstractionReponseSerializer
from .reponse_serializer_models import ModelReponse_serialize, FoodUpdateSerializer
from project.model.food_category import Foods
from project.features.food_category.data_classes import FoodDataclasses, FoodUpdatedDataClasses

class Reponse_json(AbstractionReponseSerializer):
    def serialize_create_food(self, food: Foods) -> str:
        food_data = FoodDataclasses(
            id=food.id,
            category=food.category,
            title=food.title,
            description=food.description,
            picture=food.picture,
            ingredients=food.ingredients
        )
        response = ModelReponse_serialize(food=food_data)
        return response.json()

    def serialize_update_food(self, updated_food) -> str:
        updated_foods = FoodUpdatedDataClasses(
        
            category=updated_food.category,
            title=updated_food.title,
            description=updated_food.description,
            picture=updated_food.picture,
            ingredients=updated_food.ingredients
            )
        
        response = FoodUpdateSerializer(updated_food=updated_foods)
        return response.json()

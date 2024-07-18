from .food_service.factory import FactoryFoodService
from .data_access.factory import FactoryDataAccess
from .reponse_serializer.factory import FactoryReponseSerializer
from flask import jsonify
from ...module.exception_form import FoodError
class FoodController:
    def __init__(self):
        self.data_access = FactoryDataAccess.build_object()
        self.food_service = FactoryFoodService.build_object(self.data_access)
        self.response_serializer = FactoryReponseSerializer.build_object()

    def create_foods(self, validated_data):
        try:
            food = self.food_service.create_foods(
                validated_data.category,
                validated_data.title,
                validated_data.description,
                validated_data.picture,
                validated_data.ingredients
            )
            return self.response_serializer.serialize_create_food(food)
        except FoodError as e:
            return jsonify({"error": e.to_dict()})

    def get_foods(self, food_id):
        try:
            food = self.food_service.get_foods_by_id(food_id)
            return food
        except FoodError as e:
            return jsonify({"error": e.to_dict()})

    def get_grouped_foods(self):
        try:
            grouped_foods = self.food_service.get_food_by_group()
            return grouped_foods
        except FoodError as e:
            return jsonify({"error": e.to_dict()})

    def update_food(self, food_id, validated_data):
        try:
            updated_food = self.food_service.update_food(
                food_id,
                validated_data.category,
                validated_data.title,
                validated_data.description,
                validated_data.picture,
                validated_data.ingredients
            )
            return self.response_serializer.serialize_update_food(updated_food)
        except FoodError as e:
            return jsonify({"error": e.to_dict()})

    def delete_food(self, food_id):
        try:
            deleted_food = self.food_service.delete_food(food_id)
            return deleted_food
        except FoodError as e:
            return jsonify({"error": e.to_dict()})

    def search_food(self, title):
        try:
            searched_food = self.food_service.search_food(title)
            return searched_food
        except FoodError as e:
            return jsonify({"error": e.to_dict()})

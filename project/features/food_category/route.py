from flask import Blueprint
from project.features.food_category.controller import FoodController
from .request_validator import request_validator 
from.blueprint import foods_bp
from .request_validator.pydantic_response_models import FoodPydanticModel
from ...decorators.validate import validate_schema
@foods_bp.route("/foods", methods=["POST"])
@validate_schema(FoodPydanticModel)
def create_foods(validated_data):
    controller = FoodController()
    response = controller.create_foods(validated_data)
    return response, 201

@foods_bp.route("/foods/<int:food_id>", methods=["GET"])
def get_food(food_id):
    controller = FoodController()
    response = controller.get_foods(food_id)
    return response, 200

@foods_bp.route('/foods/group', methods=["GET"])
def get_grouped_foods():
    controller = FoodController()
    response = controller.get_grouped_foods()
    return response, 200

@foods_bp.route('/foods/<int:food_id>', methods=["PUT"])
@validate_schema(FoodPydanticModel)
def update_food(food_id, validated_data):
    controller = FoodController()
    response = controller.update_food(food_id, validated_data)
    return response, 200

@foods_bp.route('/foods/<int:food_id>', methods=["DELETE"])
def delete_food(food_id):
    controller = FoodController()
    response = controller.delete_food(food_id)
    return response, 200

@foods_bp.route('/foods/search/<string:title>', methods=["GET"])
def search_food(title):
    controller = FoodController()
    response = controller.search_food(title)
    return response, 200
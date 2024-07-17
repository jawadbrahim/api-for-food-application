from flask import Blueprint
from project.features.food_category.controller import FoodController
from .request_validator import request_validator 
from.blueprint import foods_bp

@foods_bp.route("/foods", methods=["POST"])
@request_validator.validate_create_food()
def create_foods(inputs):
    controller = FoodController()
    response = controller.create_foods(inputs)
    return response, 201


@foods_bp.route("/foods/<int:food_id>",methods=["GET"])
def get_food(food_id):
    controller=FoodController()
    response=controller.get_foods(food_id)
    return response,200

@foods_bp.route('/foods/group',methods=["GET"])
def get_grouped_foods():
    controller=FoodController()
    response=controller.get_grouped_foods()
    return response,200
@foods_bp.route('/foods/<int:food_id>',methods=["PUT"])
@request_validator.validate_update_foods()
def update_food(food_id,inputs):
    controller = FoodController()
    response = controller.update_food(food_id,inputs)
    return (response), 200
@foods_bp.route('/foods/<int:food_id>', methods=["DELETE"])
def delete_food(food_id):
    controller = FoodController()
    response=controller.delete_food(food_id)
    return response

@foods_bp.route('/foods/search/<string:title>',methods=["GET"])
def search_food(title):
 
 controller=FoodController()
 response= controller.search_food(title)
 return response
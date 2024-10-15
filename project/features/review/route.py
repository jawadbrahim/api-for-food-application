from .blueprint import review_bp
from .request_validator import request_validator
from .controller import ReviewController

@review_bp.route("/review",methods=["POST"])
@request_validator.validate_create_review()
def create_review(validated_data):
    controller=ReviewController()
    response=controller.create_review(validated_data)
    return response,201
@review_bp.route("/get_review/<int:food_id>",methods=["GET"])
def get_review_by_food(food_id):
    controller=ReviewController()
    response=controller.get_review_by_food(food_id)
    return response,201
@review_bp.route("/get_reviews/<uuid:review_id>",methods=["GET"])
def get_reviews(review_id):
    controller=ReviewController()
    response=controller.get_reviews(review_id)
    return response,201
@review_bp.route("/delete_review",methods=["DELETE"])
def remove_review(review_id):
    controller=ReviewController()
    response=controller.remove_review(review_id)
    return response,201
from .controller import UserController
from .request_validator.request_validator_models import RequestValidatorModel
from project.decorators.validate import validate_schema
from project.decorators.authorization import token_required

from .blueprints import user_bp

@user_bp.route("/users",methods=["POST"])
@validate_schema(RequestValidatorModel)
@token_required
def create_user(validated_data,token_id):
    controller=UserController()
    response=controller.create_user(validated_data,token_id)
    return response,200

@user_bp.route("/users/<uuid:user_id>",methods=["GET"])

def get_users(user_id):
    controller=UserController()
    response=controller.get_user(user_id)
    return response,200
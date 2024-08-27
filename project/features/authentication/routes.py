from .blueprint import auth_bp
from .controller import AuthController
from .request_validator.request_validator_models import RegisterValidate,LoginValidate
from project.decorators.validate import validate_schema

@auth_bp.route("/register",methods=["POST"])
@validate_schema(RegisterValidate)
def register(validated_data):
    controller=AuthController()
    response=controller.register(validated_data)
    return response,201
@auth_bp.route("/login",methods=["POST"])
@validate_schema(LoginValidate)
def login(validated_data):
    controller=AuthController()
    response=controller.login(validated_data)
    return response,201
@auth_bp.route("/auth/<uuid:auth_id>",methods=["GET"])
def get_account(auth_id):
    controller=AuthController()
    response=controller.get_account(auth_id)
    return response,201
@auth_bp.route("/<string:email>",methods=["DELETE"])
def delete_account(email):
    controller=AuthController()
    response=controller.delete_account(email)
    return response,201
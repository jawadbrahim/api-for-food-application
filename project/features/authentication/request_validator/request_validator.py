from .abstraction import AbstractionRequestvalidator
from .request_validator_models import RegisterValidate,LoginValidate
from project.decorators.validate import validate_schema

class RequestValidator(AbstractionRequestvalidator):
    def validate_register(self):
        return validate_schema(json_schema=RegisterValidate)
    def validate_login(self):
        return validate_schema(json_schema=LoginValidate)
        
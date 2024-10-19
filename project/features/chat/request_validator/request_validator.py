from project.decorators.validate import validate_schema
from .request_validator_models import ChatModel
from .abstraction import AbstractionRequestvalidator

class RequestValidator(AbstractionRequestvalidator):
    def validate_create_chat(self):
        return validate_schema(json_schema=ChatModel)
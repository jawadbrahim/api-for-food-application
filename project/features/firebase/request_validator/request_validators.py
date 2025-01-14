from .abstraction import AbstractionRequestValidator
from .request_validator_model import CreateUserModel
from project.decorators.validate import validate_schema


class RequestValdiator(AbstractionRequestValidator):

 def valdiate_create_user(self):
  return validate_schema(json_schema=CreateUserModel)
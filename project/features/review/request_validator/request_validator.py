from .abstraction import AbstractionRequestValidator
from .request_validator_models import ReviewModel
from project.decorators.validate import validate_schema


class PydanticValidator(AbstractionRequestValidator):
    def validate_create_review(self):
        return validate_schema(json_schema=ReviewModel)

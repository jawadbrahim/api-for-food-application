from .abstraction import AbstractionRequestvalidator
from .pydantic_response_models import FoodPydanticModel,favoriteModel
from project.decorators.validate import validate_schema


class RequestValidator(AbstractionRequestvalidator):
    def validate_create_food(self):
        return validate_schema(json_schema=FoodPydanticModel)
    def validate_update_foods(self):
        return validate_schema(json_schema=FoodPydanticModel)
    def validate_create_favorite(self):
        return validate_schema(json_schema=favoriteModel)
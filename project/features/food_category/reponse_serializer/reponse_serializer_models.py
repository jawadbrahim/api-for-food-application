from ..data_classes import FoodDataclasses,FoodUpdatedDataClasses
from pydantic import BaseModel

class ModelReponse_serialize(BaseModel):

    food:FoodDataclasses
class FoodUpdateSerializer(BaseModel):

    updated_food:FoodUpdatedDataClasses
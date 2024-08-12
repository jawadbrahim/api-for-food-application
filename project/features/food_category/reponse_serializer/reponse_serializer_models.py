from project.features.food_category.data_classes import FoodDataclasses,FoodUpdatedDataClasses,FoodDeletedDataClasse
from pydantic import BaseModel


class ModelReponse_serialize(BaseModel):

    food:FoodDataclasses
    class Config:
     orm_mode=True
class FoodUpdateSerializer(BaseModel):

    updated_food:FoodUpdatedDataClasses
    class Config:
       orm_mode=True
class DeletedFoodSerializer(BaseModel):
    food: FoodDeletedDataClasse
    class Config:
       orm_mode=True

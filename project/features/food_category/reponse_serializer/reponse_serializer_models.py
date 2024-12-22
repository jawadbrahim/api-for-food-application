from ..data_classes import FoodDataclasses,FoodDeletedDataClasse,FoodUpdatedDataClasses,FavoriteDataClass
from pydantic import BaseModel


class ModelReponse_serialize(BaseModel):

    food:FoodDataclasses
    class config:
        orm_mode=True
   
     
class FoodUpdateSerializer(BaseModel):

    updated_food:FoodUpdatedDataClasses
    
       
class DeletedFoodSerializer(BaseModel):
    food: FoodDeletedDataClasse

class FavoriteSerializer(BaseModel):
    favorite:FavoriteDataClass
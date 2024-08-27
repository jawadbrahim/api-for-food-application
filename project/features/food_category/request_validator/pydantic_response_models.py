from pydantic import BaseModel
import uuid
class FoodPydanticModel(BaseModel):
    category: str
    title: str
    description: str
    picture: str
    ingredients: str

class favoriteModel(BaseModel):
    user_id:uuid.UUID
    food_id:int
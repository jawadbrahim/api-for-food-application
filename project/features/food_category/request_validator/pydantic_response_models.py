from pydantic import BaseModel

class FoodPydanticModel(BaseModel):
    category: str
    title: str
    description: str
    picture: str
    ingredients: str


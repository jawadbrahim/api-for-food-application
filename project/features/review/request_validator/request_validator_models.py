from pydantic import BaseModel
import uuid
class ReviewModel(BaseModel):
    user_id:uuid.UUID
    food_id:int
    rating:float
    comment:str
from pydantic import BaseModel
from typing import Literal
import uuid
class ReviewModel(BaseModel):
    user_id:uuid.UUID
    food_id:int
    rating:Literal[1,2,3,4,5]
    comment:str
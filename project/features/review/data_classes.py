from dataclasses import dataclass
from datetime import datetime
import uuid
@dataclass
class ReviewDataClasses:
    id:uuid.UUID
    user_id:uuid.UUID
    food_id:int
    rating:float
    comment:str
@dataclass
class Like:
    review_id:uuid.UUID
@dataclass
class Get_review_by_food:
     id: uuid.UUID
     user_id: uuid.UUID
     food_id: int
     rating: float
     comment: str
    
@dataclass    
class  Get_Reviews:
    review_id:uuid.UUID
@dataclass
class Delete_Review:
    review_id:uuid.UUID

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
class Get_review_by_food:
    food_id:int
@dataclass    
class  Get_Reviews:
    user_id:uuid.UUID
@dataclass
class Delete_Review:
    review_id:uuid.UUID
from dataclasses import dataclass
import uuid
from datetime import datetime
@dataclass
class FoodDataclasses:
    id: int
    category: str
    title: str
    description: str
    picture: str
    ingredients: str


@dataclass
class FoodUpdatedDataClasses:
    category: str
    title: str
    description: str
    picture: str
    ingredients: str
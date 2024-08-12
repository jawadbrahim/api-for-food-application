from dataclasses import dataclass
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
@dataclass
class FoodDeletedDataClasse:

    id :int

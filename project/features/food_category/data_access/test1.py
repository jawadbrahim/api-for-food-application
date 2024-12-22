import unittest
from unittest.mock import MagicMock
from project.features.food_category.data_access.mock import MockDataAccess
from project.features.food_category.data_access.orm_sqlalchemy import OrmSqlalchemyFoodCategory

class TestDataAccess(unittest.TestCase):
    def setUp(self):
        real_data_Access=OrmSqlalchemyFoodCategory()
        self.mock_data_access=MockDataAccess(real_data_Access)

    def test_create_food(self):
        category="meat"
        title="meatball"
        description="meatballs"
        picture="meat.png"
        ingredients=["meat","ball"]
        self.mock_data_access.create_food=MagicMock(return_value={
            "category":"meat",
            "title":"meatball",
            "description":"meatballs",
            "picture":"meat.png",
            "ingredients":["meat","ball"]
        })
        food=self.mock_data_access.create_food(category,title,description,picture,ingredients)
        self.assertEqual(food["category"],"meat")
        self.assertEqual(food["title"],"meatball")
        self.mock_data_access.create_food.assert_called_with(category,title,description,picture,ingredients)

if __name__=="__main__":
    unittest.main()

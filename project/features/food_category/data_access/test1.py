import unittest
from unittest.mock import MagicMock
from project.features.food_category.data_access.mock import MockDataAccess
from project.features.food_category.data_access.orm_sqlalchemy import OrmSqlalchemyFoodCategory

class TestGEtData(unittest.TestCase):

    def setUp(self):
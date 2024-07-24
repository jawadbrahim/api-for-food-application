from ..settings.development import Development
from ..settings.options import OrmSqlalchemyOption

from .orm_sqlalchemy import OrmSqlalchemyFoodCategory
from .mock import MockDataAccess


class FactoryDataAccess:

    @staticmethod
    def build_object(service = Development.Orm_sqlalchemy):
        if service == OrmSqlalchemyOption.ORM_SQLALCHEMY:
            return OrmSqlalchemyFoodCategory()
        
        if service == OrmSqlalchemyOption.MOCK:
            return MockDataAccess()
        raise NotImplementedError()
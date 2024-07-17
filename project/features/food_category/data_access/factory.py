from ..settings.development import Development
from ..settings.options import OrmSqlalchemyOption

from .orm_sqlalchemy import OrmSqlalchemyFoodCategory


class FactoryDataAccess:

    @staticmethod
    def build_object(service = Development.Orm_sqlalchemy):
        if service == OrmSqlalchemyOption.ORM_SQLALCHEMY:
            return OrmSqlalchemyFoodCategory()
        
        
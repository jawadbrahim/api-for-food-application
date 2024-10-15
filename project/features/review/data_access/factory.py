from ..setting.development import Development
from ..setting.option import OrmSqlAlchemyOption
from .ormsqlalchemy import OrmSqlAlchemy

class FactoryDataAccess:
 @staticmethod
 def build_object(service=Development.ORM_SQLALCHEMY):
    if service==OrmSqlAlchemyOption.ORMSQLALCHEMY:
        return OrmSqlAlchemy()
    raise NotImplementedError()
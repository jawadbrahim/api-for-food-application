from ..setting.development import Development
from ..setting.option import OrmSqlAlchemyOption
from .ormsqlalchemy import OrmSqlAlchemy

class FactoryDataAccess():

    @staticmethod
    def build_object(service=Development.ORMSQLACHEMY):
        if service == OrmSqlAlchemyOption.ORM_SQLALCHEMY:
            return OrmSqlAlchemy()
        raise NotImplementedError()
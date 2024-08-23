from ..settings.options import OrmSqlachemyOptions
from ..settings.development import Development
from .ormsqlachemy import OrmSqlalchemy

class FactoryDataAcces():
    @staticmethod
    def build_object(service=Development.ORM_SQLACHEMY):
        if service == OrmSqlachemyOptions.ORMSQLACHEMY:
            return OrmSqlalchemy()
        raise NotImplementedError()
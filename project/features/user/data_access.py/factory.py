from ..settings.options import OrmsqlalchemyOption
from ..settings.development import  Development
from .ormsqlachemy import OrmsqlalchemyDataAccess
from .mock import MockDataAccess

class FactoryDataAccess:
 @staticmethod
 def build_object(service=Development.ORM_SQLALCHEMY):
  if service == OrmsqlalchemyOption.ORMSQLALCHEMY:
   return OrmsqlalchemyDataAccess()
  if service == OrmsqlalchemyOption.MOCK:
   return MockDataAccess()
  raise NotImplementedError()
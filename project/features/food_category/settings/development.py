
from .options import (OrmSqlalchemyOption,DefaultServiceOption,SerializerOption,RequestValidateOption)


class Development:
  ORMSQLALCHEMY = OrmSqlalchemyOption.ORM_SQLALCHEMY
  DEFAULT_SERVICE = DefaultServiceOption.DEFAULT
  SERIALIZE=SerializerOption.PYDANTIC_JSON
  REQUEST_VALIDATOR=RequestValidateOption.PYDANTIC_MODEL

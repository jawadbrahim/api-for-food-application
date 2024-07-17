
from .options import (OrmSqlalchemyOption,DefaultServiceOption,SerializerOption,RequestValidateOption)


class Development:
  Orm_sqlalchemy = OrmSqlalchemyOption.ORM_SQLALCHEMY
  Default_service = DefaultServiceOption.DEFAULT
  Serialize=SerializerOption.PYDANTIC_JSON
  Request_validator=RequestValidateOption.PYDANTIC_MODEL

from .option import OrmSqlAlchemyOption,ReviewServiceOption,RequestValidatorOption,ResponseJsonOption

class Development:
    ORM_SQLALCHEMY=OrmSqlAlchemyOption.ORMSQLALCHEMY
    REVIEW_SERVICE=ReviewServiceOption.DEFAULT
    REQUEST_VALIDATOR=RequestValidatorOption.PYDANTIC_MODEL
    RESPONSE_SERIALIZER=ResponseJsonOption.PYDANTIC_JSON
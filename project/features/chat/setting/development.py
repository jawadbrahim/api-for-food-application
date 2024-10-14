from .option import OrmSqlAlchemyOption,RequestValidatorOption,SerializeOption,ServiceOption

class Development:
    ORMSQLACHEMY=OrmSqlAlchemyOption.ORM_SQLALCHEMY
    REQUEST_VALIDATOR=RequestValidatorOption.PYDANTIC_MODEL
    RESPONSE_SERIALIZE=SerializeOption.PYDANTIC_JSON
    CHAT_SERVICE=ServiceOption.DEFAULT
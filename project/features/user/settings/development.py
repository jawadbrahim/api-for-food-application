from .options import OrmsqlalchemyOption,UserServiceOption,RequestValidatorOptions,ResponseSerialzierOption

class Development:
 ORM_SQLALCHEMY=OrmsqlalchemyOption.ORMSQLALCHEMY
 USER_SERVICE=UserServiceOption.DEFAULT
 PYDANTIC_VALIDATOR=RequestValidatorOptions.PYDANTIC_MODEL
 RESPONSE_SERIALIZER=ResponseSerialzierOption.RESPONSE_JSON
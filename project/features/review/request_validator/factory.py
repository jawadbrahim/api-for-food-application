from ..setting.development import Development
from ..setting.option import RequestValidatorOption
from .request_validator import PydanticValidator


class FactoryRequestValidator:
    @staticmethod
    def build_object(service=Development.REQUEST_VALIDATOR):
        if service == RequestValidatorOption.PYDANTIC_MODEL:
            return PydanticValidator()
        raise NotImplementedError()
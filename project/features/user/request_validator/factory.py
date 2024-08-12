from ..settings.development import Development
from ..settings.options import RequestValidatorOptions

from .request_pydantic_validator import PydanticValidator


class FactoryReqeustValidator:
    @staticmethod
    def build_object(service=Development.PYDANTIC_VALIDATOR):
        if service == RequestValidatorOptions.PYDANTIC_MODEL:
            return PydanticValidator()
        raise NotImplementedError()
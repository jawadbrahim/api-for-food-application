from ..settings.options import RequestValidatorOptions
from ..settings.development import Development
from .request_validator import RequestValidator

class FactoryRequestValidator():
    @staticmethod
    def build_object(service=Development.REQUEST_VALIDATOR):
        if service == RequestValidatorOptions.PYDANTIC_MODEL:
            return RequestValidator()
        raise NotImplementedError()

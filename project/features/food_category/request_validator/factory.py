from .pydantic_response_validator import RequestValidator

from ..settings.development import Development
from ..settings.options import RequestValidateOption


class FactoryReqeustValidator():

    @staticmethod
    def build_object(service=Development.REQUEST_VALIDATOR):
        if service == RequestValidateOption.PYDANTIC_MODEL:
            return RequestValidator()
        raise NotImplementedError()
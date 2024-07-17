from .pydantic_response_validator import RequestValidator

from ..settings.development import Development
from ..settings.options import RequestValidateOption


class FactoryReqeustValidator():

    @staticmethod
    def build_object(service=Development.Request_validator):
        if service == RequestValidateOption.PYDANTIC_MODEL:
            return RequestValidator()
        raise NotImplementedError()
from ..setting.options import RequestValidatorOption
from ..setting.development import Development
from .request_validators import RequestValdiator


class FactoryRequestvalidator:
    @staticmethod
    def build_object(service=Development.REQUEST_VALIDATOR):
        if service == RequestValidatorOption.PYDANTIC_MODEL:
            return RequestValdiator()
        raise NotImplementedError()
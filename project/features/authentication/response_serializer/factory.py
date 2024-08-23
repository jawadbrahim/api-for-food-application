from ..settings.options import SerializeOptions
from ..settings.development import Development
from .response_json import RegisterSerialize

class FactoryResponseSerialize:
    @staticmethod
    def build_object(service=Development.RESPONSE_JSON):
        if service == SerializeOptions.PYDANTIC_JSON:
            return RegisterSerialize()
        raise NotImplementedError()

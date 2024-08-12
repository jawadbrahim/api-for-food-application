from ..settings.options import ResponseSerialzierOption
from ..settings.development import Development
from .pydantic_response_json import ResponseJson


class FactoryResponseJson:
    @staticmethod
    def build_object(service=Development.RESPONSE_SERIALIZER):
        if service == ResponseSerialzierOption.RESPONSE_JSON:
            return ResponseJson()
        raise NotImplementedError()
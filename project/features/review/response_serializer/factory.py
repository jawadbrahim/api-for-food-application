from ..setting.development import Development
from ..setting.option import ResponseJsonOption
from .response_serialize import Response_json

class FactoryResponseJson:
    @staticmethod
    def build_object(service=Development.RESPONSE_SERIALIZER):
        if service == ResponseJsonOption.PYDANTIC_JSON:
            return Response_json()
        raise NotImplementedError()
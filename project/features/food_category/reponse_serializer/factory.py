from ..settings.options import SerializerOption
from ..settings.development import Development
from .reponse_json import Reponse_json

class FactoryReponseSerializer():
    @staticmethod
    def build_object(service = Development.SERIALIZE):
        if service == SerializerOption.PYDANTIC_JSON:
            return Reponse_json()
        raise NotImplementedError()
        

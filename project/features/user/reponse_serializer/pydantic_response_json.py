from .pydantic_response_models import CreatedSerialzier

from .abstraction import AbstractionReponseSerializer

class ResponseJson(AbstractionReponseSerializer):
    def serialize_create_user(self,user):
        response=CreatedSerialzier(user=user)
        return response.json()
        
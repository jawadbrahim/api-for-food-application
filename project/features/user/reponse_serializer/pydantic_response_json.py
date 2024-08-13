from .pydantic_response_models import CreatedSerialzier
from ..dataclasses import UserCreated
from .abstraction import AbstractionReponseSerializer

class ResponseJson(AbstractionReponseSerializer):
    def serialize_create_user(self,user):
        user_data=UserCreated(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name
        )

        response=CreatedSerialzier(user=user_data)
        return response.json()
        
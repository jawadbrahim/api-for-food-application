from .pydantic_response_models import CreatedSerialzier,DeleteUserSerializer
from ..dataclasses import UserCreated,UserDeleted
from .abstraction import AbstractionReponseSerializer

class ResponseJson(AbstractionReponseSerializer):
    def serialize_user(self,user):
        user_data=UserCreated(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            created_at=user.created_at
        )

        response=CreatedSerialzier(user=user_data)
        return response.json()
    def serialize_delete_user(self,delete_user):
        delete_data=UserDeleted(
            id=delete_user.id
        )
        response=DeleteUserSerializer(delete_user=delete_data)
        return response.json()
        
        
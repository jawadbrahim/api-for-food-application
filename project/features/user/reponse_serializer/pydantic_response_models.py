from pydantic import BaseModel
from ..dataclasses import UserCreated,UserDeleted
class CreatedSerialzier(BaseModel):
    user:UserCreated

class DeleteUserSerializer(BaseModel):
    deleted_suser:UserDeleted

from pydantic import BaseModel
from ..dataclasses import UserCreated
class CreatedSerialzier(BaseModel):
    user:UserCreated



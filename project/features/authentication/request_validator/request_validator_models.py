from pydantic import BaseModel

class RegisterValidate(BaseModel):
    email:str
    password:str
class LoginValidate(BaseModel):
    email:str
    password:str
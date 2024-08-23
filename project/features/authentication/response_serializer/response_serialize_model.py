from pydantic import BaseModel
from ..data_classes import AuthCreated,AuthDelete,Login

class RegisterModel(BaseModel):
    account: AuthCreated
class LoginModel(BaseModel):
    account:Login
class DeletedModel(BaseModel):
    delete_account: AuthDelete
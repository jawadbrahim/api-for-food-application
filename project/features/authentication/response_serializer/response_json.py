from .abstraction import AbstractionResponseSerializer
from ..data_classes import AuthCreated,AuthDelete,Login
from .response_serialize_model import RegisterModel,DeletedModel,LoginModel

class RegisterSerialize(AbstractionResponseSerializer):
    def serialize_register(self, account):
        account = AuthCreated(
            id=account.id,
            email=account.email,
            password=account.password,
            created_at=account.created_at
        )
        response = RegisterModel(account=account)
        return response.json()
    def serialize_login(self,account):
        login_data=Login(
            id=account.id,
            email=account.email,
            password=account.password

        )
        response=LoginModel(account=login_data)
        return response.json()
    def serialize_delete_account (self, delete_account):
        deleted_accounts = AuthDelete(
            id=delete_account.id,
            email=delete_account.email,
            
            
        )
        response = DeletedModel(delete_account=deleted_accounts)
        return response.json()
    
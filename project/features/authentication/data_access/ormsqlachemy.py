from project.model.auth import Auth
from .abstraction import AbstractionDataAccess
from project.module.ormsqlachemy import OrmSqlalchemy
from ..data_classes import AuthCreated

class OrmSqlachemy(AbstractionDataAccess,OrmSqlalchemy):

    def create_account(self,email,password):
        auth=Auth(
            
           email=email,
           password=password
        )
        self.add(auth)
        return auth
    def get_account(self,email):
        auth_email=Auth.query.filter(Auth.email==email).first()
        if auth_email:
            account_data={
                "auth_id":auth_email.id,
                "email": auth_email.email,
                "password":auth_email.password
            }
        return account_data
   
      
    
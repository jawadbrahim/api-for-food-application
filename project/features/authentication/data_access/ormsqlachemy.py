from project.model.auth import Auth
from project.model.token import Token
from project.model.user import User
from .abstraction import AbstractionDataAccess
from project.module.ormsqlachemy import OrmSqlalchemy as Orm
from ..data_classes import AuthCreated

class OrmSqlalchemy(AbstractionDataAccess,Orm):

    def create_account(self, email, password):
     account = Auth(email=email, password=password)  
     self.add(account)
     return account
    def email_exists(self,email):
        exist=Auth.query.filter(Auth.email==email,
                                Auth.is_deleted == False).first()
        return exist
    def email_password_exists(self,email,password):
        account=Auth.query.filter(Auth.email==email,Auth.password==password,Auth.is_deleted==False).first()
        return account
    def get_account(self,auth_id):
        auth=Auth.query.filter(Auth.id==auth_id).first()
        if auth_id:
            account_data={
                "auth_id":auth.id,
                "email": auth.email,
                "password":auth.password
            }
        return account_data
    def insert_token(self,token_id,token_str):
        token=Token(
            id=token_id,
            token=token_str
        )
        self.add(token)
        return token
    def update_token_id(self, auth_id, token_id):
        auth_record = Auth.query.filter(Auth.id == auth_id).first()
        if auth_record:
            auth_record.token_id = token_id 
            self.commit()  
        return auth_record
    
    
         
    def delete_account(self,auth_id):
        deleted_account=Auth.query.filter(Auth.id== auth_id).first()
        if deleted_account:
            deleted_account.is_deleted=True
        return deleted_account
    
        
   
      
    
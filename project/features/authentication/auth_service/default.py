from .abstraction import AbstractionAuthService
from ..exceptions import AccountAlreadyExist,AccountNotFound,CredentialsMismatch
from project.helpers.hashing import HashingPassword
from project.helpers.jwt import JwtHelpers
from project.helpers.date import DateHelper
from ..config.jwthelpers import Config
import uuid
from project.features.authentication.data_classes import Login,AuthCreated
class Default(AbstractionAuthService):
    def __init__(self, data_access):
        self.data_access = data_access
        self.hashing = HashingPassword()
        self.jwt=JwtHelpers(Config.JWT_SECRET,Config.JWT_SIGN_ALGORITHM)
        self.date=DateHelper()

    def generate_token(self):
        token_id = uuid.uuid4()
        exp = self.date.get_expiration_date(minutes=Config.TOKEN_DURATION_IN_MINUTES)
        payload = {
            'token_id': str(token_id),
            'exp': exp
        }
        token_str = self.jwt.encode(payload)
        self.data_access.insert_token(token_id, token_str)
        return token_id, token_str


    def register(self, email, password):
     exist = self.data_access.email_exists(email)
     if exist:
        raise AccountAlreadyExist(email=email)
     hashed_password = self.hashing.hash_password(password)
     account = self.data_access.create_account(email, hashed_password)
     token_id,token_str=self.generate_token()
     self.data_access.update_token_id(account.id,token_id)
     return AuthCreated(
         email=account.id,
         password=account.password,
         created_at=account.created_at,
         token=token_str
     )



    def login(self, email, password):
        account = self.data_access.email_exists(email)
        if not account or not self.hashing.verify_password(password, account.password):
            raise CredentialsMismatch(email=email)
        
        token_id, token_str = self.generate_token()  
        self.data_access.update_token_id(account.id, token_id) 
        
        return Login(
            id=account.id,
            email=account.email,
            password=account.password,
            token=token_str
            
        )
    def get_account(self,auth_id):
        get_account=self.data_access.get_account(auth_id)
        if not get_account:
            raise AccountNotFound(auth_id=auth_id)
        return get_account
        
    def delete_account(self, auth_id):
        deleted_account = self.data_access.delete_account(auth_id)
        if not deleted_account:
            raise AccountNotFound(auth_id=auth_id)
        return deleted_account


        
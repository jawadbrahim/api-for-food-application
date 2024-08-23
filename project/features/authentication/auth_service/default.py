from .abstraction import AbstractionAuthService
from ..exceptions import AccountAlreadyExist,AccountNotFound,CredentialsMismatch
from project.helpers.hashing import HashingPassword
from project.helpers.jwt import JwtHelpers
from project.helpers.date import DateHelper
from ..config.jwthelpers import Config

class Default(AbstractionAuthService):
    def __init__(self, data_access):
        self.data_access = data_access
        self.hashing = HashingPassword()
        self.jwt=JwtHelpers(Config.JWT_SECRET,Config.JWT_SIGN_ALGORITHM)
        self.date=DateHelper()

    def generate_token(self, user_id):
     exp = self.date.get_expiration_date(minutes=Config.TOKEN_DURATION_IN_MINUTES)
     payload = {
        'user_id': str(user_id),
        'exp': exp
    }
     token_str = self.jwt.encode(payload)
     self.data_access.insert_token(user_id, token_str)  
     return token_str


    def register(self, email, password, user_id=None):
     exist = self.data_access.email_exists(email)
     if exist:
        raise AccountAlreadyExist(email=email)
     hashed_password = self.hashing.hash_password(password)
     account = self.data_access.create_account(email, hashed_password, user_id)
     return account


    def login(self, email, password):
     account = self.data_access.email_exists(email)
     if not account:
        raise CredentialsMismatch(email=email)
     if not self.hashing.verify_password(password, account.password):
        raise CredentialsMismatch(email=email)
    
    # Use the correct user_id from Auth or User as needed
     token = self.generate_token(account.user_id)  
     return {'account': account, 'token': token}

    def delete_account(self, auth_id):
        deleted_account = self.data_access.delete_account(auth_id)
        if not deleted_account:
            raise AccountNotFound(auth_id=auth_id)
        return deleted_account


        
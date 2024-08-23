from .abstraction import AbstractionAuthService
from ..exceptions import AccountAlreadyExist,AccountNotFound,CredentialsMismatch
from project.helpers.hashing import HashingPassword
from project.helpers.jwt import JwtHelpers
from project.helpers.date import DateHelper
from ..config.jwthelpers import Config
import uuid
from project.features.authentication.data_classes import Login
class Default(AbstractionAuthService):
    def __init__(self, data_access):
        self.data_access = data_access
        self.hashing = HashingPassword()
        self.jwt=JwtHelpers(Config.JWT_SECRET,Config.JWT_SIGN_ALGORITHM)
        self.date=DateHelper()

    def generate_token(self, account_id):
     token_id = uuid.uuid4()  # Generate a new UUID for the token
     exp = self.date.get_expiration_date(minutes=Config.TOKEN_DURATION_IN_MINUTES)
     payload = {
        'token_id': str(token_id),
        'exp': exp
    }
     token_str = self.jwt.encode(payload)
     self.data_access.insert_token(token_id, token_str)
     return token_str


    def register(self, email, password):
     exist = self.data_access.email_exists(email)
     if exist:
        raise AccountAlreadyExist(email=email)
     hashed_password = self.hashing.hash_password(password)
     account = self.data_access.create_account(email, hashed_password)
     return account


    def login(self, email, password):
     account = self.data_access.email_exists(email)
     if not account or not self.hashing.verify_password(password, account.password):
        raise CredentialsMismatch(email=email)

    # Generate token using the account's ID
     token = self.generate_token(account.id)
    
    # Extract the UUID from the token payload to update the token_id
     decoded_token = self.jwt.decode(token)
     token_uuid = decoded_token['token_id']
    

     self.data_access.update_token_id(account.id, token_uuid)


     return Login(
        
        id=account.id,
        email=account.email,
        password=account.password
    )

    def delete_account(self, auth_id):
        deleted_account = self.data_access.delete_account(auth_id)
        if not deleted_account:
            raise AccountNotFound(auth_id=auth_id)
        return deleted_account


        
from dataclasses import dataclass


@dataclass
class Config:
    TOKEN_DURATION_IN_MINUTES = 60
    JWT_SECRET = 'secret_key'
    JWT_SIGN_ALGORITHM = 'HS256'
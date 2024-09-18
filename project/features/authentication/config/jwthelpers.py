from dataclasses import dataclass
from project.config.development import Development

@dataclass
class Config:
    TOKEN_DURATION_IN_MINUTES = 60
    JWT_SECRET = Development.JWT_SECRET
    JWT_SIGN_ALGORITHM = 'HS256'
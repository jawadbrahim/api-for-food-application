import os
from dataclasses import dataclass

@dataclass
class Development:
    DATABASE_URL = os.getenv('DATABASE_URL')
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    JWT_SECRET = os.getenv("JWT_SECRET")
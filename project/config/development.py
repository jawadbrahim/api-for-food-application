import os
from dataclasses import dataclass
from redis import Redis
@dataclass
class Development:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT =os.getenv("REDIS_PORT")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    JWT_SECRET=os.getenv("JWT_SECRET")
   
    

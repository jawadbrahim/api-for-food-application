import os
from dataclasses import dataclass

@dataclass
class Development:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = (os.getenv("REDIS_PORT"))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    MONGO_URI= os.getenv("MONGO_URI")
    MONGO_NAME=os.getenv("MONGO_NAME")

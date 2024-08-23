from dataclasses import dataclass
from datetime import datetime
import uuid
@dataclass
class AuthCreated:
    id:uuid.UUID
    email:str
    password:str
    created_at: datetime
@dataclass
class Login:
    id:uuid.UUID
    email:str
    password:str
@dataclass
class AuthDelete:
    id: uuid.UUID
    email: str
    
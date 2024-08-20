from dataclasses import dataclass
import datetime
import uuid
@dataclass
class AuthCreated:
    id=uuid.UUID
    email:str
    password:str
    created_at: datetime
from dataclasses import dataclass
import uuid

@dataclass
class UserCreated:
    id:uuid.UUID
    first_name:str
    last_name:str
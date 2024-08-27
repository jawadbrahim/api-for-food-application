from dataclasses import dataclass
import uuid
import datetime

@dataclass
class UserCreated:
    id:uuid.UUID
    first_name:str
    last_name:str
@dataclass
class UserDeleted:

  id:uuid.UUID
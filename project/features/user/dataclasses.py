from dataclasses import dataclass
import uuid
from datetime import datetime

@dataclass
class UserCreated:
    id:uuid.UUID
    first_name:str
    last_name:str
    created_at:datetime
@dataclass
class UserDeleted:

  id:uuid.UUID
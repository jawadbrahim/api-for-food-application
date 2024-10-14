from database.postgres import db
from dataclasses import dataclass
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class Room(db.Model):
    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    creator_id=db.Column(UUID(as_uuid=True),nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))

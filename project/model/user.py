from database.postgres import db
from dataclasses import dataclass
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):

    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    first_name=db.Column(db.String(20))
    last_name=db.Column(db.String(20))
    is_deleted=db.Column(db.Boolean,default=False)
    created_at=db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))
    updated_at=db.Column(db.DateTime,onupdate=datetime.datetime.now(datetime.timezone.utc))
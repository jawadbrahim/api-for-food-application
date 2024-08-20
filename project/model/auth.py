from database.postgres import db
from dataclasses import dataclass
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime

@dataclass
class Auth(db.Model):
  id = db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
  email=db.Column(db.String(100))
  password=db.Column(db.String(100))
  created_at=db.column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc()))
  is_deleted=db.Column(db.Boolean,default=False)
  user_id=db.Column("user_id",UUID(as_uuid=True),db.ForeignKey("user.id"),nullable=True)
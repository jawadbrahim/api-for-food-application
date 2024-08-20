from database.postgres import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime

@dataclass

class Token(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    token = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc()))
    is_deleted=db.Column(db.Boolean,default=False)
    user_id = db.Column("user_id", UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=True)
from database.postgres import db
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID
from dataclasses import dataclass

@dataclass
class Chat(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    sender_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False)
    receiver_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    is_archived = db.Column(db.Boolean, default=False)

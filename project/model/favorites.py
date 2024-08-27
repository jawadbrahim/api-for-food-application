from database.postgres import db
from dataclasses import dataclass
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime
from sqlalchemy.orm import relationship
@dataclass
class Favorite(db.Model):

    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    user_id = db.Column("user_id", UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=True)
    food_id = db.Column("food_id", db.Integer, db.ForeignKey("foods.id"), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    food = relationship("Foods", backref="favorites")

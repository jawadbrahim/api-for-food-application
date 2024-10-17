from database.postgres import db
from dataclasses import dataclass
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime


@dataclass
class Review(db.Model):
    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    rating=db.Column(db.Float,nullable=False)
    comment=db.Column(db.Text,nullable=False)
    is_deleted=db.Column(db.Boolean,default=False)
    created_at=db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))
    likes=db.Column(db.Integer,default=0)
    dislikes=db.Column(db.Integer,default=0)
    user_id=db.Column("user_id",UUID(as_uuid=True),db.ForeignKey("user.id"),nullable=False)
    food_id=db.Column("food_id",db.Integer,db.ForeignKey("foods.id"),nullable=False)
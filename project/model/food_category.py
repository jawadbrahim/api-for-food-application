from database.postgres import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime
from dataclasses import dataclass

@dataclass
class FoodStatus:
    ACTIVE='ACTIVE'
    DELETED="DELETED"



class Foods(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String(200))
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    picture = db.Column(db.String(600))
    ingredients = db.Column(db.String(1000))
    created_at=db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=True)
    status=db.Column(db.String,default=FoodStatus.ACTIVE)
    
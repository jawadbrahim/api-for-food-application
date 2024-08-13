from database.postgres import db
from dataclasses import dataclass
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime



@dataclass
class AuthStatus:
    ACTIVE="ACTIVE"
    DELETE="DELETE"
@dataclass
class Auth(db.Model):
    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    email=db.Column(db.String)
    password=db.Column(db.String)
    created_at=db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))
    status=db.Column(db.String,default=AuthStatus.ACTIVE)
    user_id=db.Column("user_id",UUID(as_uuid=True),db.ForeignKey("user.id"),nullable=True,unique=True)
 
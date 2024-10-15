# from dataclasses import dataclass
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# from database.postgres import db
# import datetime


# @dataclass
# class ChatRead(db.Model):
#     id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
#     chat_id=db.Column("chat_id",UUID(as_uuid=True),db.ForeignKey("chat.id"),nullable=True)
#     user_id=db.Column(UUID(as_uuid=True),nullable=False)
#     read_it= db.Column(db.DateTime,default=datetime.datetime.now(datetime.timezone.utc))


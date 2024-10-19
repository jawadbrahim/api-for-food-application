from pydantic import BaseModel
import uuid
class ChatModel(BaseModel):
    message:str
    sender_id:uuid.UUID
    receiver_id:uuid.UUID
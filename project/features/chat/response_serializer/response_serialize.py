from .abstraction import AbstractionResponseSerializer
from .reponse_serialize_model import SerializeChat
from ..data_classes import ChatClass

class Serialize_json(AbstractionResponseSerializer):
    def serialize_create_chat(self,chat):
        chat_data=ChatClass(
            id=chat.id,
            message=chat.message,
            sender_id=chat.sender_id,
            receiver_id=chat.receiver_id,
            created_at=chat.created_at
            
        )
        response=SerializeChat(chat=chat_data)
        return response.json()
            
        
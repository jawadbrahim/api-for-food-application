from .abstraction import AbstractionService
from ..exception import UserNotFound
from ..helper.encrypted import Encrypt
import base64
class Default(AbstractionService):
    def __init__(self,data_access):
        self.data_access=data_access
        self.encrypt=Encrypt()
        


    def create_chat(self, message, sender_id, receiver_id):
     encrypted_message = self.encrypt.encrypted_message(message)
     encrypted_message_base64 = base64.b64encode(encrypted_message).decode('utf-8')
     chat = self.data_access.create_chat(encrypted_message_base64, sender_id, receiver_id)
     if not chat:
        raise UserNotFound(sender_id=sender_id)
     channel=f"chat_{receiver_id}"
    
     self.redis_client.publish(channel, chat.id)
     return chat
    def get_chat(self, chat_id):
     chat = self.data_access.get_chat(chat_id)
     if not chat:
        raise UserNotFound(chat_id=chat_id)
     encrypted_message = base64.b64decode(chat.message.encode('utf-8'))
     decrypted_message = self.encrypt.decrypted_message(encrypted_message)
     return decrypted_message
    def archived_chat(self,chat_id):
        chat_to_archive=self.data_access.archived_chat(chat_id)
        if chat_to_archive:
          raise UserNotFound()
        return chat_to_archive
    def mark_as_read(self,user_id,chat_id):
        marked_chat=self.data_access.mark_as_read(user_id,chat_id)
        if not marked_chat:
            raise UserNotFound()
        return marked_chat

        
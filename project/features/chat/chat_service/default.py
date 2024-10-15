# from .abstraction import AbstractionService
# from ..exception import UserNotFound
# from ..helper.encrypted import Encrypt
# from project.config.development import Development
# class Default(AbstractionService):
#     def __init__(self,data_access):
#         self.data_access=data_access
#         self.encrypt=Encrypt()
#         self.redis_client=Development.redis_client


#     def create_chat(self,message,room_id):
#         encrypted_message=self.encrypt.encrypted_message(message)
#         chat=self.data_access.create_chat(encrypted_message)
#         if not chat:
#             raise UserNotFound()
#         self.redis_client.publish(f"room_{room_id}",encrypted_message)
#         return chat
#     def get_chat(self,chat_id):
#         chat=self.data_access.get_chat(chat_id)
#         if not chat:
#             raise UserNotFound()
#         decrypted_message=self.encrypt.decrypted_message(chat.message)
#         return decrypted_message
#     def archived_chat(self,chat_id):
#         chat_to_archive=self.data_access.archived_chat(chat_id)
#         if chat_to_archive:
#           raise UserNotFound()
#         return chat_to_archive
#     def mark_as_read(self,user_id,chat_id):
#         marked_chat=self.data_access.mark_as_read(user_id,chat_id)
#         if not marked_chat:
#             raise UserNotFound()
#         return marked_chat

        
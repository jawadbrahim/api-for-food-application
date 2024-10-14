from .abstraction import AbstractionDataAccess
from project.module.ormsqlachemy import OrmSqlalchemy as orm
from project.model.chat import Chat
from project.model.chatread import ChatRead


class OrmSqlAlchemy(AbstractionDataAccess,orm):
    def create_chat(self,message,sender_id,receiver_id,room_id):
        chat=Chat(
            message=message,
            sender_id=sender_id,
            receiver_id=receiver_id,
            room_id=room_id
        )
        return self.add(chat)
    def get_chat(self,chat_id):
        get_chat=Chat.query.filter(Chat.id==chat_id,Chat.is_deleted==False).first()
        return get_chat
    def delete_chat(self,chat_id):
        chat_delted=Chat.query.filter(Chat.id==chat_id).first()
        if chat_delted:
            chat_delted.is_deleted=True
        return chat_delted
    def archived_chat(self,chat_id):
        chat_to_archive=Chat.query.filter(Chat.id==chat_id).first()
        if chat_to_archive:
            chat_to_archive.is_archived=True
        return chat_to_archive
    def mark_as_read(self,user_id,chat_id):
        marked_chat=ChatRead(
            user_id=user_id,
            chat_id=chat_id
        )
        self.add(marked_chat)
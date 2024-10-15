# from .data_access.factory import FactoryDataAccess
# from .chat_service.factory import FactoryService
# from .response_serializer.factory import FactorySerialze
# from .exception import UserNotFound
# from flask import jsonify
# class ChatController:


#     def __init__(self):
#         self.data_access=FactoryDataAccess.build_object()
#         self.chat_service=FactoryService.build_object(self.data_access)
#         self.response_serializer=FactorySerialze.build_object()


#     def create_chat(self,validated_data):
#         try:
#          chat=self.chat_service.create_chat(validated_data.message)
#          self.data_access.commit()
#          return self.response_serializer.serialize_create_chat(chat)
#         except(UserNotFound,Exception)as e:
#            return jsonify({"error":e.to_dict()})
#     def get_chat(self,chat_id):
#        try:
#           get_chat=self.chat_service.get_chat(chat_id)
#           return get_chat
#        except(UserNotFound,Exception)as e:
#           return jsonify({"error":e.to_dict()})
     
    
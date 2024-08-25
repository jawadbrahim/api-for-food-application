from .user_service.factory import FactoryUserService
from .data_access.factory import FactoryDataAccess
from .reponse_serializer.factory import FactoryResponseJson
from project.redis.redis_cache import Rediscache
from .exceptions import UserNotExist,FailedToCreateUser
from flask import jsonify

class UserController:
    def __init__(self):
      self.data_access=FactoryDataAccess.build_object()
      self.response_serializer=FactoryResponseJson.build_object()
      self.user_service=FactoryUserService.build_object(self.data_access)
      # self.redis_cache=Rediscache()

    def create_user(self, validated_data, token_id):
     try:
        user = self.user_service.create_user(
            validated_data.first_name,
            validated_data.last_name,
            token_id=token_id
        )
        self.data_access.commit()  
        return self.response_serializer.serialize_create_user(user)
     except (FailedToCreateUser, Exception) as e:
        return jsonify({"error": e.to_dict()})
    
    def get_user(self,user_id):
       try:
         get_users= self.user_service.get_user_by_id(user_id)
         return get_users
          
          

       except (UserNotExist,Exception) as e :
          return jsonify({"error": e.to_dict()})
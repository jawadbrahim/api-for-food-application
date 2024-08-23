from .data_access.factory import FactoryDataAcces
from .auth_service.factory import FactoryAuthService
from .response_serializer.factory import FactoryResponseSerialize
from .exceptions import AccountAlreadyExist,AccountNotFound,CredentialsMismatch
from flask import jsonify
class AuthController:
      def __init__(self):
        self.data_access=FactoryDataAcces.build_object()
        self.auth_serice=FactoryAuthService.build_object(self.data_access)
        self.response_serializer=FactoryResponseSerialize.build_object()

      def register(self, validated_data):
       try:
        account = self.auth_serice.register(validated_data.email, validated_data.password)
        self.data_access.commit()
        return self.response_serializer.serialize_register(account)
       except AccountAlreadyExist as e:
        return jsonify({"error": e.to_dict()})
      def login(self, validated_data):
       try:
        account = self.auth_serice.login(validated_data.email, validated_data.password)
        self.data_access.commit()
        return self.response_serializer.serialize_login(account)
       except (CredentialsMismatch, Exception) as e:
        return jsonify({"error": str(e)})
      def delete_account(self,auth_id):
        try:
         deleted_account=self.auth_serice.delete_account(auth_id)
         self.data_access.commit()
         return self.response_serializer.serialize_delete_account(deleted_account)
        except AccountNotFound as e:
            return jsonify({"error": e.to_dict()}), 404
       
      
       
from .abstraction import AbstractionDataAccess
from project.module.ormsqlachemy import OrmSqlalchemy
from project.model.user import User
from project.model.token import Token


class  OrmsqlalchemyDataAccess(AbstractionDataAccess,OrmSqlalchemy):
    def create_user(self, first_name, last_name):
     user = User(first_name=first_name, last_name=last_name)
     self.add_and_flush(user)
     return user
    def is_token_in_use(self, token_id):
     token = Token.query.filter_by(id=token_id).first()
     if token:
        if token.user_id:
            return True
     return False
    def update_token_user_id(self, token_id, user_id):
     token = Token.query.filter_by(id=token_id).first()
     if token:
        token.user_id = user_id 
        return True
     return False
    def get_user_by_id(self,user_id):
     user=User.query.filter(User.id==user_id,User.is_deleted==False).first()
     if  user:
        user_data={
          
           "id":user.id,
           "first_name":user.first_name,
           "last_name" :user.last_name
        }
        return user_data
    def delete_user(self,user_id):
      food_deleted=User.query.filter(User.id==user_id).first()
      if food_deleted:
        food_deleted.is_deleted=True
      return food_deleted

      

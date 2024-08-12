from .abstraction import AbstractionDataAccess
from project.module.ormsqlachemy import OrmSqlalchemy
from project.model.user import User


class  OrmsqlalchemyDataAccess(AbstractionDataAccess,OrmSqlalchemy):


    def create_user(self,first_name,last_name):
        user=User(
            first_name=first_name,
            last_name=last_name
        )
        self.add(user)
        return user
    def get_user_by_id(self,user_id):
     user=User.query.filter(User.id==user_id).first()
     if  user:
        user_data={
           
           "first_name":user.first_name,
           "last_name" :user.last_name
        }
        return user_data
     

    
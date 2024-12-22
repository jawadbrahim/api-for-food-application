from database.postgres import db
from sqlalchemy import func
class OrmSqlalchemy():

    def add(self,obj):
        db.session.add(obj)
    def add_and_flush(self, obj):
        db.session.add(obj)
        db.session.flush()
    def commit(self):

        db.session.commit()
    def delete(self,obj):
        db.session.delete(obj)
    def scalar(self,query):
     return db.session.query(query).scalar()
    def count(self,obj):
        return func.count(obj)
    
    
from database.postgres import db

class OrmSqlalchemy():

    def add(self,obj):
        db.session.add(obj)
    def commit(self):

        db.session.commit()
    def delete(self,obj):
        db.session.delete(obj)
from .abstraction import AbstractionDataAccess
from project.model.review import Review
from project.module.ormsqlachemy import OrmSqlalchemy as orm

class OrmSqlAlchemy(AbstractionDataAccess,orm):

    def create_review(self,user_id,food_id,rating,comment):
        review=Review(
            user_id=user_id,
            food_id=food_id,
            rating=rating,
            comment=comment
        )
        self.add(review)
        return review
    def get_review_by_food(self,food_id):
        get_review=Review.query.filter(Review.food_id==food_id,Review.is_deleted==False).first()
        return get_review
    def get_reviews(self,review_id):
        get_reviews=Review.query.filter(Review.id==review_id,Review.is_deleted==False).all()
        return get_reviews
    def delete_review(self,review_id):
        delete_review=Review.query.filter(Review.id==review_id).first()
        if delete_review:
            delete_review.is_deleted=True
        return delete_review

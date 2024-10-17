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
    def get_review_by_id(self,review_id):
        review=Review.query.filter(Review.id==review_id,Review.is_deleted==False).first()
        return review
    def get_review_by_food(self, food_id):
        reviews = Review.query.filter(Review.food_id == food_id, Review.is_deleted == False).all()
        if reviews:
            review_data = [
                {
                    "id": review.id,
                    "user_id": review.user_id,
                    "food_id": review.food_id,
                    "rating": review.rating,
                    "comment": review.comment,
                    "created_at": review.created_at
                }
                for review in reviews
            ]
            return review_data
        return []
    def delete_review(self,review_id):
        delete_review=Review.query.filter(Review.id==review_id).first()
        if delete_review:
            delete_review.is_deleted=True
        return delete_review

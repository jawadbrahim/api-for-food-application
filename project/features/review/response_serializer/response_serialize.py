from .abstraction import AbstractionResponseSerializer
from .response_serialize_models import DeleteReview,CreateReview,GetReviewByFood,GetReviews
from ..data_classes import ReviewDataClasses,Get_review_by_food,Get_Reviews,Delete_Review


class Response_json(AbstractionResponseSerializer):

    def serialize_create_review(self,review):
        review_data=ReviewDataClasses(
            id=review.id,
            user_id=review.user_id,
            food_id=review.food_id,
            rating=review.rating,
            comment=review.comment
        )
        response=CreateReview(review=review_data)
        return response.json()
    def serialzie_get_review_by_food(self,get_review):
        review_data=Get_review_by_food(
            food_id=get_review.food_id
        )
        response=GetReviewByFood(get_review=review_data)
        return response.json()
    def serialze_get_reviews(self,get_reviews):
        reviews_data=Get_Reviews(
            user_id=get_reviews.user_id
        )
        response=GetReviews(get_reviews=reviews_data)
        return response.json()
    def serialize_delete_reviews(self,delete_review):
        delete_reviews=Delete_Review(
            review_id=delete_review.review_id
        )
        response=DeleteReview(delete_review=delete_reviews)
        return response.json()
        

        

        
            
        
            
        

        
            
        
    



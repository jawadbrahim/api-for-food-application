from .abstraction import AbstractionResponseSerializer
from .response_serialize_models import DeleteReview,CreateReview,GetReviewByFood,GetReviews,LikeReview,DislikeReview
from ..data_classes import ReviewDataClasses,Get_review_by_food,Get_Reviews,Delete_Review,Like


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
    def serialize_Like_review(self,like_review):
       like_data=Like(
          review_id=like_review.id
       )
       response=LikeReview(like_review=like_data)
       return response.json()
    def serialize_Dislike_review(self,dislike_review):
       dislike_data=Like(
          review_id=dislike_review.id
       )
       response=DislikeReview(dislike_review=dislike_data)
       return response.json()
       
    def serialzie_get_review_by_food(self, get_review):
        review_data = [
            Get_review_by_food(
                id=review['id'],                
                user_id=review['user_id'],    
                food_id=review['food_id'],
                rating=review['rating'],       
                comment=review['comment'],      
                created_at=review['created_at'] 
            )
            for review in get_review
        ]
        response = GetReviewByFood(get_review=review_data)
        return response.json()
    def serialze_get_reviews(self, get_reviews):
     reviews_data = [
        Get_Reviews(
            review_id=review.id
        )
        for review in get_reviews
     ]
     response = GetReviews(get_reviews=reviews_data)
     return response.json()

    def serialize_delete_reviews(self,delete_review):
        delete_reviews=Delete_Review(
            review_id=delete_review.id
        )
        response=DeleteReview(delete_review=delete_reviews)
        return response.json()
        

        

        
            
        
            
        

        
            
        
    



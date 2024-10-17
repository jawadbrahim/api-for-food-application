from .abstraction import AbstractionService
from ..exceptions import FoodNotFound,ReviewNotFound

class Default(AbstractionService):

    def __init__(self,data_acces):
        self.data_access=data_acces
    
    def create_review(self,user_id,food_id,rating,comment):
        review=self.data_access.create_review(user_id,food_id,rating,comment)
        if not review:
            raise FoodNotFound()
        return review
    def like_review(self,review_id):
        likes_review=self.data_access.get_review_by_id(review_id)
        
        if not likes_review:
            raise ReviewNotFound(review_id=review_id)
        if likes_review.likes is None:
            likes_review.likes = 0
        likes_review.likes += 1

        return likes_review
    def dislike_review(self,review_id):
        dislikes_review=self.data_access.get_review_by_id(review_id)
        if not dislikes_review:
            raise ReviewNotFound(review_id=review_id)
        if dislikes_review.dislikes is None:
            dislikes_review.dislikes = 0
        dislikes_review.dislikes += 1
        return dislikes_review 
    def get_review_by_food(self,food_id):
        get_review=self.data_access.get_review_by_food(food_id)
        if not get_review:
            raise FoodNotFound()
        return get_review
    def delete_review(self,review_id):
        deleted_review=self.data_access.delete_review(review_id)
        if not deleted_review:
            raise ReviewNotFound(review_id=review_id)
        return deleted_review
    
    


        
        
        

        

    

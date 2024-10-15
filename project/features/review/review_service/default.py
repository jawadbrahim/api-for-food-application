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
    def get_review_by_food(self,food_id):
        get_review=self.data_access.get_review_by_food(food_id)
        if not get_review:
            raise FoodNotFound()
        return get_review
    def get_reviews(self,review_id):
        get_reviews=self.data_access.get_reviews(review_id)
        if not get_reviews:
            raise ReviewNotFound(review_id=review_id)
        return get_reviews
    def delete_review(self,review_id):
        deleted_review=self.data_access.delete_review(review_id)
        if not deleted_review:
            raise ReviewNotFound(review_id=review_id)
        return deleted_review
    
    


        
        
        

        

    

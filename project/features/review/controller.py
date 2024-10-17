from .data_access.factory import FactoryDataAccess
from .response_serializer.factory import FactoryResponseJson
from .review_service.factory import FactoryReviewService
from .exceptions import ReviewNotFound,FoodNotFound
from flask import jsonify

class ReviewController:
    def __init__(self):
        self.data_access=FactoryDataAccess.build_object()
        self.review_service=FactoryReviewService.build_object(self.data_access)
        self.response_serializer=FactoryResponseJson.build_object()


    def create_review(self,validated_data):
        try:
         review=self.review_service.create_review(validated_data.user_id,validated_data.food_id,validated_data.rating,validated_data.comment)
         self.data_access.commit()
         return self.response_serializer.serialize_create_review(review)
        except(FoodNotFound,Exception)as e:
           return jsonify({"error":e.to_dict()})
    def  like_review(self,review_id):
      try:
        likes_review=self.review_service.like_review(review_id)
        self.data_access.commit()
        return self.response_serializer.serialize_Like_review(likes_review)
      except(ReviewNotFound,Exception)as e:
         return jsonify({"error":e.to_dict()})
    def dislike_review(self,review_id):
       try:
          dislikes_review=self.review_service.dislike_review(review_id)
          self.data_access.commit()
          return self.response_serializer.serialize_Dislike_review(dislikes_review)
       except(ReviewNotFound,Exception)as e:
          return jsonify({"error":e.to_dict()})
    def get_review_by_food(self,food_id):
       try:
          get_review=self.review_service.get_review_by_food(food_id)
          return self.response_serializer.serialzie_get_review_by_food(get_review)
       except(FoodNotFound,Exception)as e:
          return jsonify({"error":e.to_dict()})
    def remove_review(self,review_id):
       try:
        delete_review=self.review_service.delete_review(review_id)
        self.data_access.commit()
        return self.response_serializer.serialize_delete_reviews(delete_review)
       except(ReviewNotFound,Exception)as e:
          return jsonify({"error":e.to_dict()})

    
       
    



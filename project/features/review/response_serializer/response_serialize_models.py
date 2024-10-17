from pydantic import BaseModel
from ..data_classes import ReviewDataClasses,Get_review_by_food,Get_Reviews,Delete_Review,Like


class CreateReview(BaseModel):
    review:ReviewDataClasses
class GetReviewByFood(BaseModel):
    get_review:list[Get_review_by_food]
class GetReviews(BaseModel):
    get_reviews: list[Get_Reviews] 
class DeleteReview(BaseModel):
    delete_review:Delete_Review
class LikeReview(BaseModel):
    like_review:Like
class DislikeReview(BaseModel):
    dislike_review:Like
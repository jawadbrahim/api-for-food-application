from pydantic import BaseModel
from ..data_classes import ReviewDataClasses,Get_review_by_food,Get_Reviews,Delete_Review


class CreateReview(BaseModel):
    review:ReviewDataClasses
class GetReviewByFood(BaseModel):
    get_review:Get_review_by_food
class GetReviews(BaseModel):
    get_reviews:Get_Reviews
class DeleteReview(BaseModel):
    delete_review:Delete_Review
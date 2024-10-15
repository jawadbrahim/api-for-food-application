from project.module.exception_form import AppError

class FoodNotFound(AppError):
    description="food not found"
    http_code=404
class ReviewNotFound(AppError):
    description="review not found"
    http_code=404

from ...module.exception_form import AppError

    
class FoodFailedToCreate(AppError):
   description="filed to create food"
   http_code=404
class FoodNotExist(AppError):
    description="food not found"
    http_code=404

class GroupedFoodIsEmpty(AppError):
    description="category not found"
    http_code=404
class TitleNotFound(AppError):
   description="title not found"
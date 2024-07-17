from ...module.exception_form import FoodError

    
class FoodFailedToCreate(FoodError):
    def __init__(self, **kwargs):
        super().__init__("failet to create food", 404, **kwargs)
class FoodNotExist(FoodError):
    def __init__(self, **kwargs):
        super().__init__("food does not exist", 404, **kwargs)

class GroupedFoodIsEmpty(FoodError):
    def __init__(self, **kwargs):
        super().__init__(" category not exist", 404, **kwargs)
class TitleNotFound(FoodError):
    def __init__(self,**kwargs):
        super().__init__("this food not found",404,**kwargs)
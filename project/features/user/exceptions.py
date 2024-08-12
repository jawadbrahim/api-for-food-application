from project.module.exception_form import FoodError


class FailedToCreateUser(FoodError):
     def __init__(self, **kwargs):
        super().__init__("failet to create user", 404, **kwargs)
class UserNotExist(FoodError):
    def __init__(self, **kwargs):
        super().__init__("user not exixt", 404, **kwargs)

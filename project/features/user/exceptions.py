from project.module.exception_form import AppError


class FailedToCreateUser(AppError):
    description="failed to create user"
    http_code=404
class UserNotExist(AppError):
    description="user does not exist"
    http_code=404
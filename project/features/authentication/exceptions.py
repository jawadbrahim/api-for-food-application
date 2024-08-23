from project.module.exception_form import AppError

class AccountAlreadyExist(AppError):
    description="account already exist"
    http_code=404
class AccountNotFound(AppError):
    description="account not found"
    http_code=404
class CredentialsMismatch(AppError):
    description="email or password not match"
    http_code=404
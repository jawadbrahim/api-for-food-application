from pydantic import BaseModel
class RequestValidatorModel(BaseModel):
    first_name:str
    last_name:str
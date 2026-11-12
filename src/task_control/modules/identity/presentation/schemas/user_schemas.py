
from pydantic import EmailStr,BaseModel , Field

class UserCreateRequest(BaseModel):
    email:EmailStr
    password:str=Field(min_length=5,description="Modt de pass d'au moins 12 caractere")

class UserResponse(BaseModel):
    id:int
    email:EmailStr



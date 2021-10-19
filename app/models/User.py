from pydantic import BaseModel, Field
from beanie import Document
from pydantic.networks import EmailStr


class UserModel(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(..., max_length=75)


class UserField(UserModel):
    user_name: str = Field(..., max_length=75)


class User(Document, UserField):
    pass

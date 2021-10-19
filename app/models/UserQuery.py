from pydantic import BaseModel, Field
from beanie import Document
from pydantic.networks import EmailStr


class UserQueryModel(BaseModel):
    username: str = Field(..., max_length=75)
    phone: str = Field(...)
    email: EmailStr = Field(...)
    message: str = Field(..., max_length=75)


class UserQuery(Document, UserQueryModel):
    pass

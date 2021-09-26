from pydantic import Field
from beanie import Document
from pydantic.networks import EmailStr


class UserQuery(Document):
    username: str = Field(..., max_length=75)
    phone:str = Field(...)
    email:EmailStr = Field(...)
    message: str = Field(..., max_length=75)

from pydantic import Field
from beanie import Document
from pydantic.networks import EmailStr


class User(Document):
    user_name: str = Field(..., max_length=75)
    email:EmailStr = Field(...)
    password: str = Field(..., max_length=75)

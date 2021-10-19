from typing import List
from pydantic import Field
from beanie import Document, PydanticObjectId


class LikedRecipe(Document):
    user_id: PydanticObjectId = Field(...)
    liked_recipes: List[str] = Field(...)

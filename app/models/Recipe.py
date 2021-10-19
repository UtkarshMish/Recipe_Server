from typing import List
from beanie import Document
from pydantic import Field
from pydantic.main import BaseModel
from pydantic.types import OptionalIntFloatDecimal


class Nutrition(BaseModel):
    protein: str = Field(...)
    fat: str = Field(...)
    calories: str = Field(...)
    carbohydrates: str = Field(...)
    cholesterol: str = Field(...)
    sodium: str = Field(...)


class Recipe(Document):
    name: str = Field(...)
    total_time: str = Field(...)
    ingredients: List[str] = Field(...)
    description: list = Field(...)
    breadcrumbs: List[str] = Field(...)
    img_link: str = Field(...)
    ratings: OptionalIntFloatDecimal = Field(...)
    serving_count: OptionalIntFloatDecimal = Field(...)
    nutrition: Nutrition = Field(...)

    class Collection:
        name: str = "Cuisines"

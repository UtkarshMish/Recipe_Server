from typing import Optional
from pydantic import BaseModel, Field


class PageSearch(BaseModel):
    page_no: int = Field(1)
    query: Optional[str]

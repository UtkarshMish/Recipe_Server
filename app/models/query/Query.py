from typing import List
from pydantic import BaseModel, Field


class QueryJson(BaseModel):
    queryString: List[str] = Field(...)

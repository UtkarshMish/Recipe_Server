from typing import Optional
from .Token import Token


class LikedQuery(Token):
    recipe_id: Optional[str]
    recommendation: bool
    liked: Optional[bool]
    user: str

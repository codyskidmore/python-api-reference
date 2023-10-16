from typing import Optional

from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None

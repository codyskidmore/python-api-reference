from typing import Optional, Dict

from pydantic import BaseModel


class UpdatePost(BaseModel):
    title: str = None
    content: str = None
    published: bool = False
    rating: Optional[int] = None

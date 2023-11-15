from typing import Optional, Dict

from pydantic import BaseModel


class UpdatePost(BaseModel):
    id: int
    data: Dict

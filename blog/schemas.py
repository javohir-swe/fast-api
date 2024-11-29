from pydantic import BaseModel
from typing import Optional
from database import Base


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False

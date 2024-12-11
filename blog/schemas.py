from pydantic import BaseModel
from typing import Optional
from blog.database import Base


class Blog(BaseModel):
    title: str
    body: str
    # published: Optional[bool] = False

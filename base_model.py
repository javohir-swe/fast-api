from importlib.metadata import requires
from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {"success": True, "title": request.title}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

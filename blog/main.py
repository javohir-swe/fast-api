import uvicorn
from fastapi import FastAPI

from blog.schemas import Blog



app = FastAPI()


@app.post('/blog')
def create_blog(request: Blog):
    return {
        "success": True,
        "data": {
            "title": request.title,
            "body": request.body,
            "published": request.published,
        }
    }



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

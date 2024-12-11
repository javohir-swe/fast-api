import uvicorn
from fastapi import FastAPI, Depends

from blog import models
from blog.database import engine, SessionLocal
from blog.schemas import Blog

from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# {
#     "success": True,
#     "data": {
#         "title": request.title,
#         "body": request.body,
#         "published": request.published,
#     }
# }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

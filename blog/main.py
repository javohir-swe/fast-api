import uvicorn
from fastapi import FastAPI, Depends, Response, HTTPException, status

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


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request: Blog, db: Session = Depends(get_db)):
    """This API can create a blog"""

    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def get_blogs_list(db: Session = Depends(get_db)):
    """This API can return all blogs list"""

    blogs = db.query(models.Blog).all()
    return {"success": True, "data": blogs}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog_detail(id: int, response: Response, db: Session = Depends(get_db)):
    """this API can return the blog of that particular ID based on the given ID"""

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return {"success": True, "data": blog}
    else:
        response.status_code=status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No blog found with id {id}")
        # return {"status_code": response.status_code, "error": f"No blog found with id {id}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

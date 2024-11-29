from typing import Optional, Union

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"data": {"key": "Value"}}


@app.get('/about')
def about():
    return {
        "success": True,
        "data": {
            "page-name": "About Page!!!"
        }
    }

@app.get('/blog')
def blog(limit: int = 10, published: bool = False, sort: Optional[str] = None, q: Union[str, None] = None):
    if published:
        if sort:
            return {'data': f'limit={limit}, published={published}, sort={sort}, p={q}'}
        else:
            return {'data': f'limit={limit}, published={published}, p={q}'}
    else:
        return {'data': f'{limit} data unpublished, p={q}'}

@app.get('/blog/unpublished')
def unpublished_blogs():
    return {'data': 'All unpublished blogs'}


@app.get('/blog/{blog_id}')
def blog_detail(blog_id: int):
    return {'data': blog_id}


@app.get('/blog/{blog_id}/comments')
def comment(blog_id: int):
    return {
        'data': {
            f"blog_{blog_id}": {
                '1',
                '2',
                '3'
            }
        }
    }

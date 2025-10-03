from fastapi import HTTPException, status
from schemas import Blog, UpdateBlog
from models import Blog as BlogModel



def get_blogs(db):
    blogs = db.query(BlogModel).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No blogs available")
    return blogs

def get_blog(id: int, db):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog

def delete_blog(id, db):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    db.delete(blog)
    db.commit()
    return {"detail": "Blog deleted successfully"}

def create_blog(request: Blog, db):
    new_blog = BlogModel(title=request.title, body=request.body, published=request.published, user_id=4)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    if not new_blog:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Blog creation failed")
    return new_blog

def update_blog(id: int, request: UpdateBlog, db):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    # note: only update fields that are provided in the request
    new_title = request.title if request.title is not None else blog.title
    new_body = request.body if request.body is not None else blog.body
    blog.title = new_title
    blog.body = new_body
    # blog.update(request)
    db.commit()
    db.refresh(blog)
    return blog
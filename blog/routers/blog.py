from fastapi import APIRouter, Depends, status
from schemas import Blog, UpdateBlog, ShowBlog, CreateUser
from database import get_db
from sqlalchemy.orm import Session
from typing import List
from repository.blog import get_blogs, get_blog, delete_blog, create_blog, update_blog
from auth2 import get_current_user

router = APIRouter(
    prefix="/blog", tags=["blogs"]
)


# create the database tables
@router.post("/", status_code=status.HTTP_201_CREATED)
def createBlog(request: Blog, db: Session = Depends(get_db), current_user: CreateUser = Depends(get_current_user)):
    return create_blog(request, db)


# get all blogs
@router.get("/", response_model=List[ShowBlog], status_code=status.HTTP_200_OK)
def allBlogs(db: Session = Depends(get_db), current_user: CreateUser = Depends(get_current_user)):
    return get_blogs(db)

# get a single blog by id
@router.get("/{id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
def getBlog(id: int, db: Session = Depends(get_db), current_user: CreateUser = Depends(get_current_user)):
    return get_blog(id, db)
    

# delete a blog by id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(id, db: Session = Depends(get_db), current_user: CreateUser = Depends(get_current_user)):
    return delete_blog(id, db)



# update a blog by id
@router.put("/{id}", response_model=ShowBlog ,status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id: int, request: UpdateBlog, db: Session = Depends(get_db), current_user: CreateUser = Depends(get_current_user)):
    return update_blog(id, request, db)

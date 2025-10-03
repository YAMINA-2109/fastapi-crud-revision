from fastapi import APIRouter, Depends, status
from schemas import CreateUser, ShowUser, UpdateUser
from database import get_db
from sqlalchemy.orm import Session
from typing import List
from repository.user import getUser, getUsers, createUser, updateUser, deleteUser


user_router = APIRouter(
    prefix="/user", tags=["users"]
)


# create a user
@user_router.post("/" , response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request : CreateUser, db: Session = Depends(get_db)):
    return createUser(request, db)

# get all users
@user_router.get("/", response_model=List[ShowUser] ,status_code=status.HTTP_200_OK)
def get_users(db: Session= Depends(get_db)):
    return getUsers(db)

# get a single user by id
@user_router.get("/{id}", response_model=ShowUser, status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    return getUser(id, db)

# delete a user by id
@user_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id : int, db : Session = Depends(get_db)):
    return deleteUser(id, db)


# update a user 
@user_router.put("/{id}", response_model=ShowUser, status_code = status.HTTP_202_ACCEPTED)
def update_user(id: int, request: UpdateUser, db: Session = Depends(get_db)):
    return updateUser(id, request, db)
from fastapi import HTTPException, status
from schemas import CreateUser, UpdateUser
from models import User as UserModel
from hashing import Hash



def createUser(request : CreateUser, db):
    created_user = UserModel(name= request.name, email= request.email, password= Hash.bcrypt(request.password), is_active= request.is_active)
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    if not created_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User creation failed")
    return created_user


def getUsers(db):
    users = db.query(UserModel).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users available")
    return users

# get a single user by id
def getUser(id: int, db):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return user

# delete a user by id
def deleteUser(id : int, db ):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}


# update a user 
def updateUser(id: int, request: UpdateUser, db):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with the id {id} is not available")
    # user.update(request)
    new_name = request.name if request.name is not None else user.name
    new_mail = request.email if request.email is not None else user.email
    new_pswd = Hash.bcrypt(request.password) if request.password is not None else user.password
    new_is_active = request.is_active if request.is_active is not None else user.is_active
    user.name = new_name
    user.email = new_mail
    user.password = new_pswd
    user.is_active = new_is_active
    db.commit()
    db.refresh(user)
    return user
from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from models import User as UserModel
from hashing import Hash
from JWTtoken import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from schemas import Token
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login", response_model=Token,status_code=status.HTTP_200_OK)
def login(request:OAuth2PasswordRequestForm = Depends() , db: Session = Depends(get_db)):    
    user = db.query(UserModel).filter(UserModel.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    # generate and return a token 
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
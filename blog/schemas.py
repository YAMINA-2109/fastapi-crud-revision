from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True

class Blog(BlogBase):
    model_config = {
        "from_attributes": True
    }


class UpdateBlog(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    published: Optional[bool] = None


class CreateUser(BaseModel):
    name : str
    email : str
    password : str
    is_active : Optional[bool] = True

class ShowUser(BaseModel):
    name : str
    email : str
    is_active : bool
    blogs : list[Blog] = []
    model_config = {
        "from_attributes": True
    }


class UpdateUser(BaseModel):
    name : Optional[str] = None
    email : Optional[str] = None
    password : Optional[str] = None
    is_active : Optional[bool] = True

class ShowBlog(BlogBase):
    creator: Optional[ShowUser] = None
    model_config = {
        "from_attributes": True
    }

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

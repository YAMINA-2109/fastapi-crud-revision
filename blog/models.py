from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base, engine
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean, default=True)
    
    # clé étrangère qui pointe vers users.id
    user_id = Column(Integer, ForeignKey("users.id"))

    # côté many-to-one
    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

        # relation one-to-many: un user a plusieurs blogs
    blogs = relationship("Blog", back_populates="creator")

Base.metadata.create_all(engine)

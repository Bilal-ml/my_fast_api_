from .database import Base
from sqlalchemy import Integer, String, Boolean, Column, ForeignKey
from sqlalchemy.sql.expression import text, null
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
class Post(Base):
    __tablename__ = "post"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at =Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User")
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    email=Column(String, nullable=False)
    password=Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    
class Vote(Base):
    __tablename__ ="vote"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id", ondelete="CASCADE"), primary_key=True)
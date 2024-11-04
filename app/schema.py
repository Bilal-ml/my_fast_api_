from pydantic import BaseModel, EmailStr,Field
from typing import Optional
from typing_extensions import Annotated
from datetime import datetime
class PostBase(BaseModel):
    title: str
    content: int
    published: bool = True
    
class postcreate(PostBase):
    pass 
    
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    
class post(BaseModel):
    title: str
    content: int
    published: bool =True
    id: int
    user_id: int
    user: UserOut
    
class postOut(BaseModel):
    Post:post
    votes:int

    
   
class user(BaseModel):
    email: EmailStr
    password: str
    
class UserRes(BaseModel):
    email: EmailStr
    password: str
    id:int
    
class Token(BaseModel):
    access_token:str
    token_type: str


class Token_data(BaseModel):
    id: Optional[int] 
    

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(strict=True, le=1)]
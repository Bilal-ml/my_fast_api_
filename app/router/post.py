from fastapi import APIRouter, status, HTTPException,Depends, Response
from ..schema import postcreate, post,postOut
from sqlalchemy.orm import Session
from ..database import get_db
from ..model import Post, Vote
from .auth import get_current_user
from typing import List
from sqlalchemy import func
router = APIRouter(prefix="/posts")

@router.get("/", response_model=List[postOut])
def get_post(db: Session = Depends(get_db), current_user:int = Depends(get_current_user)):
    #post = db.query(Post).all()
    result = db.query(Post, func.count(Vote.post_id).label("votes")).join(Vote, Vote.post_id == Post.id, isouter=True).group_by(Post.id).all()
    return result
    
@router.post("/", response_model=post)
def create_post(post: postcreate, db: Session = Depends(get_db), current_user:int = Depends(get_current_user)):
    post= Post(user_id = current_user.id, **post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.get("/{id}")
def find_post(id:int, db:Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()
    
    return post
@router.delete("/{id}", )
def delete(id:int, db:Session =Depends(get_db), current_user:int = Depends(get_current_user)):
    post_query = db.query(Post).filter(Post.id ==id)
    post =post_query.first()
    if post == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id } not found")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

from fastapi import APIRouter, status, HTTPException, Depends
from ..database import get_db
from sqlalchemy.orm import Session
from ..model import User
from ..schema import user
from ..utils import hash
router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user:user, db: Session =Depends(get_db)):
    hashed_password = hash(user.password)
    user.password = hashed_password
    user = User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
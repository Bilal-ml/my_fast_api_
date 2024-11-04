from fastapi import APIRouter, Depends, status,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schema, model,utils
from .auth import create_access_token
router = APIRouter(prefix="/login",
                   tags=['Authentication'])
@router.post('/')
def login(user_credential:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    user = db.query(model.User).filter(model.User.email ==user_credential.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
        
    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    access_token = create_access_token({'user_id': user.id})
        
    return {"access_token": access_token, "token_type": "bearer"}


from fastapi import status, HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..database import get_db
from ..model import User
from ..schema import Token_data
from ..confih import settings
auth_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY=settings.secret_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTE =settings.access_token_expire_minutes

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({'exp':expire})
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return jwt_token
def token_verify(token:str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id = payload.get("user_id")
        if user_id == None:
            raise credential_exception
        token_data = Token_data(id= user_id)
        
    except JWTError:
        raise credential_exception
    return token_data


def get_current_user(token:str = Depends(auth_scheme), db:Session = Depends(get_db) ):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate credential",
                                         headers={"WWW-Authenticate":"Bearer"})
    Token_data = token_verify(token, credential_exception)
    user = db.query(User).filter(User.id == Token_data.id).first()
    return user


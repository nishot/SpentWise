import jwt
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from datetime import datetime,timedelta,timezone
from .config import setting
from . import utilis,schema,database,model
from sqlalchemy.orm import Session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=setting.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, setting.secret_key, algorithm=setting.algorithm)
    return encoded_jwt




def verify_access_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,setting.secret_key,algorithms=[setting.algorithm])

        id:int | None =payload.get("users_id")
        if id is None:
            raise credentials_exception
        
        token_data=schema.TokenData(user_id=id)
    except InvalidTokenError:
        raise credentials_exception
    
    return token_data

def get_current_user(token:str =Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data=verify_access_token(token,credentials_exception)
    print(token_data.user_id)
    user=db.query(model.User).filter(model.User.users_id==token_data.user_id).first()
    if user is None:

        raise credentials_exception
    
    return user
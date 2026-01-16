from .. import database , schema,model,utilis,oAuth2
from sqlalchemy.orm import Session
from fastapi import Body,Response,status,HTTPException,Depends,APIRouter
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(prefix="/login",
                 tags=['login'])



@router.post("/",response_model=schema.Token)
def login(credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(model.User).filter(model.User.email==credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail={"Invalid credentials"})
    if not utilis.verify_password(credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail={"Invalid credentials"})
    
    access_token=oAuth2.create_access_token(data={"users_id":user.users_id})
    return {"access_token":access_token,"token_type":"bearer"}
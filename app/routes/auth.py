from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, model, schema, utilis, oAuth2

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/", response_model=schema.Token)
def login(
    credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = db.query(model.User).filter(
        model.User.email == credentials.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials",
        )

    if not utilis.verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials",
        )

    access_token = oAuth2.create_access_token(
        data={"users_id": user.users_id}
    )
    return {"access_token": access_token, "token_type": "bearer"}
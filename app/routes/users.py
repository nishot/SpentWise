from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import database, model, schema, utilis, oAuth2

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schema.UserResponse,
)
def create_user(
    user: schema.UserCreate,
    db: Session = Depends(database.get_db),
):
    hashed_password = utilis.get_password_hash(user.password)
    user.password = hashed_password
    user_create = model.User(**user.model_dump())
    db.add(user_create)
    db.commit()
    db.refresh(user_create)
    return user_create


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[schema.UserResponse],
)
def user_show(
    db: Session = Depends(database.get_db),
    current_user: model.User = Depends(oAuth2.get_current_user),
):
    users = db.query(model.User).all()
    return users


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    db: Session = Depends(database.get_db),
    current_user: model.User = Depends(oAuth2.get_current_user),
):
    user = db.query(model.User).filter(
        model.User.users_id == user_id
    ).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if user.users_id != current_user.users_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this user",
        )

    db.delete(user)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

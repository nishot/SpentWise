from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import database, model, schema, oAuth2

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schema.Categories,
)
def create_categories(
    categories: schema.Categories,
    db: Session = Depends(database.get_db),
    current_user: model.User = Depends(oAuth2.get_current_user),
):
    new_category = model.Categories(
        owner_id=current_user.users_id, **categories.model_dump()
    )
    existing = db.query(model.Categories).filter(
        model.Categories.name == new_category.name
    ).first()

    if existing is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Category already exists",
        )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.get("/", response_model=list[schema.CategoriesReturn])
def show_categories(
    db: Session = Depends(database.get_db),
    current_user: model.User = Depends(oAuth2.get_current_user),
):
    categories = db.query(model.Categories).filter(
        model.Categories.owner_id == current_user.users_id
    ).all()
    return categories

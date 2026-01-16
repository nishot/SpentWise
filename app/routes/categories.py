from .. import utilis,model,database,schema,oAuth2
from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session

router=APIRouter(prefix="/categories",tags=['categories'])


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.Categories)
def create_categories (categories:schema.Categories,db:Session=Depends(database.get_db),current_user:model.User=Depends(oAuth2.get_current_user)):
    categories=model.Categories(owner_id=current_user.users_id,**categories.model_dump())
    query=db.query(model.Categories).filter(model.Categories.name==categories.name).first()
    if query is  None:
        db.add(categories)
        db.commit()
        db.refresh(categories)
        return categories
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="categories exists")
    

@router.get("/",response_model=list[schema.categories_return])
def show_categories(db:Session=Depends(database.get_db),current_user:model.User=Depends(oAuth2.get_current_user)):
    listofcategories=db.query(model.Categories).filter(current_user.users_id==model.Categories.owner_id).all()
    return listofcategories

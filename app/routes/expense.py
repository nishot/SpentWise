from .. import utilis,model,database,schema,oAuth2
from fastapi import APIRouter,status,HTTPException,Depends,Response
from sqlalchemy.orm import Session

router=APIRouter(prefix="/expense",tags=['Expenses'])



@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.expense_return)
def create_expense(expenses:schema.expense,
                   db:Session=Depends(database.get_db),
                   current_user:model.User=Depends(oAuth2.get_current_user)):
    

    expenses=model.Expenses(user_id=current_user.users_id,**expenses.model_dump())
    db.add(expenses)
    db.commit()
    db.refresh(expenses)
    return expenses


@router.get("/",response_model=list[schema.expense_return])
def show_exenses(db:Session=Depends(database.get_db),current_user:model.User=Depends(oAuth2.get_current_user)):
    listofexpense=db.query(model.Expenses).filter(current_user.users_id==model.Expenses.user_id).all()
    return listofexpense


@router.delete("/{id}")
def del_expenses(id:int,db:Session=Depends(database.get_db),current_user:model.User=Depends(oAuth2.get_current_user)):
    expenses=db.query(model.Expenses).filter(model.Expenses.expense_id==id).first()

    if expenses is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"detail not found"})
    if expenses.owner.users_id != current_user.users_id:
        raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Not authorized to update this expense"
    )
    db.delete(expenses)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_expense(
    id: int,
    expense: schema.expense,
    db: Session = Depends(database.get_db),
    current_user: model.User = Depends(oAuth2.get_current_user)
):
    expenses = db.query(model.Expenses)\
                 .filter(model.Expenses.expense_id == id)\
                 .first()
    

    if expenses is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found"
        )

    if expenses.owner.users_id!=current_user.users_id :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this expense"
        )

    for key, value in expense.model_dump().items():
        setattr(expenses, key, value)

    db.commit()
    db.refresh(expenses)

    return expenses


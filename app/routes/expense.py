from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import database, model, schema, oAuth2

router = APIRouter(prefix="/expense", tags=["Expenses"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schema.ExpenseReturn,
)
def create_expense(
    expense: schema.Expense,
    db: Session = Depends(database.get_db),
    current_user: model.User = Depends(oAuth2.get_current_user),
):
    new_expense = model.Expenses(
        user_id=current_user.users_id, **expense.model_dump()
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@router.get("/", response_model=list[schema.ExpenseReturn])
def show_expenses(
    db: Session = Depends(database.get_db),
    current_user: model.User = Depends(oAuth2.get_current_user),
):
    expenses = db.query(model.Expenses).filter(
        model.Expenses.user_id == current_user.users_id
    ).all()
    return expenses


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: model.User = Depends(oAuth2.get_current_user),
):
    expense = db.query(model.Expenses).filter(
        model.Expenses.expense_id == id
    ).first()

    if expense is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    if expense.owner.users_id != current_user.users_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this expense",
        )

    db.delete(expense)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_expense(
    id: int,
    expense_data: schema.Expense,
    db: Session = Depends(database.get_db),
    current_user: model.User = Depends(oAuth2.get_current_user),
):
    expense = db.query(model.Expenses).filter(
        model.Expenses.expense_id == id
    ).first()

    if expense is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    if expense.owner.users_id != current_user.users_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this expense",
        )

    for key, value in expense_data.model_dump().items():
        setattr(expense, key, value)

    db.commit()
    db.refresh(expense)
    return expense

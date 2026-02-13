from datetime import datetime

from pydantic import BaseModel, EmailStr, NonNegativeFloat


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    users_id: int
    email: EmailStr
    created_on: datetime

    class Config:
        from_attributes = True


class Login(BaseModel):
    email: EmailStr
    password: str


class Categories(BaseModel):
    name: str


class CategoriesReturn(Categories):
    categories_id: int


class Expense(BaseModel):
    categories_id: int
    title: str
    amount: NonNegativeFloat


class ExpenseReturn(Expense):
    expense_id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int | None = None
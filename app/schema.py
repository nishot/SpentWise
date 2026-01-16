from pydantic import BaseModel,EmailStr,NonNegativeFloat
from sqlalchemy.orm import Relationship
from datetime import datetime

class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserResponse(BaseModel):
    users_id:int
    email:EmailStr
    created_on:datetime
    
    class Config:
        from_attribute=True


class Login(BaseModel):
    email:EmailStr
    password:str


class Categories(BaseModel):
    name:str

class categories_return(Categories):
    categories_id:int

class expense(BaseModel):
    # id, title, amount, user_id (FK), category_id (FK)
    categories_id:int
    title:str
    amount:NonNegativeFloat

class expense_return(expense):
    expense_id:int
    Relationship()


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int | None = None
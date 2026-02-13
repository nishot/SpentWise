from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func, Numeric
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    users_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_on = Column(DateTime, server_default=func.now())


class Categories(Base):
    __tablename__ = "categories"

    categories_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    owner_id = Column(
        Integer,
        ForeignKey("users.users_id", ondelete="CASCADE"),
        nullable=False,
    )

    user = relationship("User")


class Expenses(Base):
    __tablename__ = "expenses"

    expense_id = Column(Integer, primary_key=True, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    title = Column(String(255), nullable=False)
    user_id = Column(
        Integer,
        ForeignKey("users.users_id", ondelete="CASCADE"),
        nullable=False,
    )
    categories_id = Column(
        Integer,
        ForeignKey("categories.categories_id", ondelete="CASCADE"),
        nullable=False,
    )

    owner = relationship("User")
    category = relationship("Categories")
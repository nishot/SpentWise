from fastapi import FastAPI, status

from . import model, database
from .routes import users, auth, categories, expense

model.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(expense.router)


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Welcome to SpentWise"}

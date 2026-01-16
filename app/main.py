from fastapi import FastAPI,status
from .routes import users,auth,categories,expense
from . import model ,database


model.Base.metadata.create_all(bind=database.engine)
app=FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(expense.router)

@app.get("/",status_code=status.HTTP_200_OK)
def root():
    return {" Welcome to SPENTWISE "}



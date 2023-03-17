from . import models
from .database import engine , SessionLocal, get_db
from .routers import employee, user, authentication
from fastapi import FastAPI

app = FastAPI()

#This will create a table inn Database
models.Base.metadata.create_all(bind=engine)

#API Router config
#Registering Router
app.include_router(employee.router)
app.include_router(user.router)
app.include_router(authentication.router)

#Creating database instance
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

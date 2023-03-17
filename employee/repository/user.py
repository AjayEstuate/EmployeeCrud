''' USER SERVICE LAYER '''

from sqlalchemy.orm import Session
from .. import schema, database,models
from fastapi import FastAPI, Depends, status, Response, HTTPException
from passlib.context import CryptContext

#Password hashing 
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto" )

def create_user(request: schema.User,db : Session):
       #Hashing Password
    hashedPassword = pwd_cxt.hash(request.password) 
    new_user = models.User(name=request.name, password = hashedPassword, email = request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request 

def get_user(id:int, db:Session= Depends):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{id} User not found ')
    return user
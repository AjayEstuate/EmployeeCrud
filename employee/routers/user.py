from fastapi import FastAPI, Depends, status, Response, HTTPException,APIRouter
from .. import schema, database,models
from typing import List
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from ..repository import user
 

router = APIRouter( tags=['USER'] , prefix="/user")

get_db = database.get_db



@router.post('/', response_model= schema.ShowUser)
def create_user(request: schema.User,db : Session = Depends(get_db)):
 return user.create_user(request, db, )

@router.get("/{id}",response_model= schema.ShowUser) 
def get_user(id:int, db:Session= Depends(get_db)):
    return user.get_user(id, db)
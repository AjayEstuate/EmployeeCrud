'''EMPLOYEE CONTROLLER LAYER'''
from fastapi import APIRouter
from .. import schema, database,models, oaut2
from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..repository import employee


router = APIRouter(tags=["EMPLOYEE"], prefix="/emp")

get_db = database.get_db

@router.get("/", status_code= status.HTTP_200_OK, response_model= List[schema.ShowEmployee]) #Using response model to get only required details of an object
def get_All(response: Response, db : Session = Depends(get_db), get_current_user : schema.User = Depends(oaut2.get_current_user) ):
   return employee.get_all_employees(db)

@router.post('/',  status_code=status.HTTP_201_CREATED)
def create(emp: schema.CreatingEmployee, db : Session = Depends(get_db), get_current_user : schema.User = Depends(oaut2.get_current_user)):
    return employee.create(emp , db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, emp:schema.UpdatingEmployee , db : Session = Depends(get_db), get_current_user : schema.User = Depends(oaut2.get_current_user)):
    return employee.update(id, emp, db)
   
@router.get("./{arg}", status_code= status.HTTP_200_OK, response_model= schema.ShowEmployee)
def get_Employee_by_Username_or_ID(arg, response: Response, db : Session = Depends(get_db), get_current_user : schema.User = Depends(oaut2.get_current_user)):
    return employee.get_Employee_By_Name(arg,response,db)

@router.get("/{id}", status_code= status.HTTP_200_OK, response_model= schema.ShowEmployee)
def get_Employee(id, response: Response, db : Session = Depends(get_db), get_current_user : schema.User = Depends(oaut2.get_current_user)):
    return employee.get_Employee(id,response,db)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete(id, db : Session = Depends(get_db), get_current_user : schema.User = Depends(oaut2.get_current_user) ):
    return employee.delete(id, db)
    


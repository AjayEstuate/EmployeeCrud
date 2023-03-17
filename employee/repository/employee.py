''' EMPLOYEE SERVICE LAYER '''
from sqlalchemy import engine
from sqlalchemy.orm import Session
from .. import schema, database,models
from fastapi import FastAPI, Depends, status, Response, HTTPException
from datetime import datetime
import re



def valid_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)): return True
    else: return False
    
'''Getitng all Employee in a List'''
def get_all_employees(db:Session):
    employees = db.query(models.Employee).all()
    return employees

'''CREATING'''
def create(emp:schema.CreatingEmployee, db:Session):
    #Validating for Username and email id
    employee = db.query(models.Employee).filter(models.Employee.username == emp.username)
    if len(emp.username)<4:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Invalid USER NAME Format')
    if  employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User Name Already Exsist')
    employee = db.query(models.Employee).filter(models.Employee.email == emp.email)
    if  employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Email ID  Already Exsist')
    if  not valid_email(emp.email):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Email ID  Format')
    #Creating Employee Object
    new_emp = models.Employee(username = emp.username.lower(), fullname = emp.fullname.upper(), email = emp.email.lower() , user_id=1)
    new_emp.createdate = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

'''UPDTING'''
def update(id, emp:schema.UpdatingEmployee , db : Session):
    employee = db.query(models.Employee).filter(models.Employee.id == id).first()
    if  not valid_email(emp.email):
        raise HTTPException(status_code=status.WS_1003_UNSUPPORTED_DATA, detail=f'Invalid Email ID  Format')
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{id} Employee id not found ')
    else:
        #If new and old email id are same Assaigning email id
        if employee.email == emp.email:
            employee.email = emp.email.lower()
        else: #If both are NOT same, Assaigning email id
             #Checking email is already exsists or not
            if db.query(models.Employee).filter(models.Employee.email == emp.email.lower()).first():  
              raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Email ID Already Exsist')
            #Re-initializing Email id
            employee.email = emp.email.lower()

        employee.fullname = emp.fullname.upper() 
        employee.updatedate =  datetime.now().strftime("%d/%m/%Y %H:%M:%S")   
        db.commit()
        db.refresh(employee)
        return employee
    
"""GETTING BY ID OR NAME"""
def get_Employee_By_Name(arg, response: Response, db : Session):
    emp = db.query(models.Employee).filter(models.Employee.id == arg).first()
    if not emp:
       emp = db.query(models.Employee).filter(models.Employee.username == arg).first()
       if not emp: #Throwing HTTPException
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee Not Found ")
    return emp
 
"""GETTING BY ID"""
def get_Employee(id, response: Response, db : Session):
    emp = db.query(models.Employee).filter(models.Employee.id == id).first()
    if not emp: #Throwing HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Emp ID {id} Not found in DataBase  ")
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {f"Emp ID {id} Not found in DataBase  "}
    return emp

'''DELETE'''
def delete(id, db : Session):
    employee = db.query(models.Employee).filter(models.Employee.id == id)
    if not employee.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{id} Employee id not found ')
    employee.delete(synchronize_session=False)
    db.commit()
    return {f"Emp ID {id} Deleted Sucesfully  "}
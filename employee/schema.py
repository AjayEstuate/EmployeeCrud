from pydantic import BaseModel
from typing import Optional, List, Union

class Employee(BaseModel):
    id       : Optional[int]
    username : str
    fullname : str
    email    : str
    createdate : Optional[str]
    updatedate : Optional[str]

    class Config():
        orm_mode = True

class CreatingEmployee(BaseModel):
    username : str
    fullname : str
    email    : str
class UpdatingEmployee(BaseModel):
    fullname : str
    email    : str


class User(BaseModel):
    name : str
    password : str
    email : str

#It is used as Data Transfer Object 
#TO show only required attributes we use this ResponseModel
class ShowUser(BaseModel):
    name : str
    email : str
    employees : List[Employee]=[]
    class Config():
        orm_mode = True


class ShowEmployee(BaseModel):
    fullname : str
    email : str
    creator : ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    email : str
    password : str

#JWT Token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
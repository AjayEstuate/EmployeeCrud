

from fastapi import APIRouter, Depends,  HTTPException, status
from .. import schema, database,models, token
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



router = APIRouter( tags=["AUTHENTICATION"])

from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

@router.post('/login')
def login( request: OAuth2PasswordRequestForm = Depends()  , db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'INVALID USER NAME')
    
    if not pwd_cxt.verify(request.password, user.password ):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Incorrect Password")
    
    #Generate a Jwt token and return
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    return user


# def validate_user(request: OAuth2PasswordRequestForm = Depends()  , db:Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.email == request.username).first()
#     if not user:
#          user = db.query(models.User).filter(models.User.name == request.username).first()
#          if  user:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'INVALID USER NAME')
#     return user     

# @router.post('/login')
# def login( request: OAuth2PasswordRequestForm = Depends()  , db:Session = Depends(database.get_db)):

#     user = validate_user(request, db)
#     if not pwd_cxt.verify(request.password, user.password ):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Incorrect Password")
    
#     #Generate a Jwt token and return
#     access_token = token.create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}
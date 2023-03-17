from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .database import Base

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, index= True, autoincrement=True)
    username = Column( String(10), unique= True)
    fullname = Column( String(20))
    email = Column( String(20), unique= True , nullable= False )
    createdate = Column( String(255))
    updatedate = Column( String(255))
    #ForeignKey
    user_id = Column(Integer, ForeignKey('user.id'))
    #Creating relationship between 2 tables 
    creator = relationship("User", back_populates= "employees")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index= True, autoincrement=True)
    name = Column( String(20))
    password = Column(String(65))
    email = Column( String(20))
    #Creating relationship between 2 tables 
    employees = relationship('Employee', back_populates="creator")
     
     
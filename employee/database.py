from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DataBase Config
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/python_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Creating database instance
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
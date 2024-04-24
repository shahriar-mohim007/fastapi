from pydantic import BaseModel,SecretStr,Json,HttpUrl,validator
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductORM(Base):
    __tablename__ = 'products'
    prodId = Column(Integer, primary_key=True, nullable=False)
    prodName = Column(String(63), unique=True)
    price = Column(Float)
    stock = Column(Integer)

class Employee(BaseModel):
    ID: str
    pwd: SecretStr
    salary: int
    details: Json
    FBProfile: HttpUrl

    @validator('ID')
    def alphanum(cls, x):
        if x.isalnum()==False:
          raise (ValueError('Must be alphanumeric'))

class Product(BaseModel):
    prodId:int
    prodName:str
    price:float
    stock:int
    class Config:
      from_attributes = True
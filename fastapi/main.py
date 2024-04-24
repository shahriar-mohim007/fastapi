from fastapi import FastAPI, Path, Query
import uvicorn
from typing import Optional
from models import Product,ProductORM
productlist=[]
app = FastAPI()


@app.get("/home")
async def index():
    return {"message": "Hello World"}

@app.get("/employee/{name}/{age}")
async def user(name:str, age:Optional[int]=None):
    return {"name":name, "age":age}

@app.get("/employee")
async def get_employee(branch_id:int,name:str=Path(...,min_length=10), brname:str=Query(None, min_length=5, max_length=10), age:Optional[int]=None):
    employee={'name':name, 'Branch':brname, 'Branch ID':branch_id, 'age':age}
    return employee


@app.post("/product/")
async def addnew(product:Product):
   product=Product(prodId=2, prodName='LED Bulb', price=250,stock=50)
   prod_alchemy=ProductORM(**product.dict())
   return prod_alchemy
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8089,
    reload=True)
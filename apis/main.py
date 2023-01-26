from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

myDb = []

class Basket(BaseModel):
    id: int
    name: str
    price: float
    product1: str
    product2: Optional[str] = None
    
    
@app.get("/")
def read_root():
    return {"Hi": "Help us add products to our Database"}

@app.get("/baskets")
def get_products():
    return myDb

@app.get("/baskets/{basket_id}")
def get_a_product(basket_id: int):
    basket = basket_id -1
    return myDb[basket]

@app.post("/baskets")
def add_product(basket: Basket):
    myDb.append(basket.dict())
    return myDb[-1]

@app.delete("baskets/{basket_id}")
def delete_basket(basket_id: int):
    myDb.pop(basket_id-1)
    return{"task": "delete successful"}
    

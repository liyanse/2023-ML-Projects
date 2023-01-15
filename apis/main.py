from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import Gender,User


app = FastAPI()

## The database
db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Lians",
        last_name= "Wanjiku",
        gender= Gender.female     
        ),
    User(
        id=uuid4(), 
        first_name="Shem",
        last_name= "Githinji",
        gender= Gender.male   
        )
]

@app.get("/")
async def root():
    return {"message": "Lians"}

@app.get("/api.v1/users")
async def fetch_users():
    return db;
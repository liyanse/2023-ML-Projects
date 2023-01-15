from typing import List
from uuid import UUID
from fastapi import FastAPI

from models import Gender,User


app = FastAPI()

## The database
db: List[User] = [
       User(
        id=UUID("20ddb18d-2de8-4db7-b66b-767c8343318e"), 
        first_name="Lians",
        last_name= "Wanjiku",
        gender= Gender.female     
        ),
    User(
        id=UUID("166e7941-9837-4502-94d0-21375263b534"), 
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

##How to add a new user 

@app.post("/api.v1/users")
async def register_new_user(user: User):
    db.append(user)
    return {"id": user.id}

##How to send our post request to our API

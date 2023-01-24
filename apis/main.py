## FASTAPI  is a modern fast web framework for builfing APIs with Python 3.6+
##based on standard Python type hints. It's built on top of Starlette for the 
## web parts and Pydantic for the data parts. Some of its key features include:
## 1. Fast Performance          2. Easy to use
## 3. Fast to code              3. Short
## 5. Fewer bugs                6. Standard


## Path Parameters
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

#Create an Enum class¶
#Import Enum and create a sub-class that inherits from str and from Enum.
#By inheriting from str the API docs will be able to know that the values must be of type string and will be able to render correctly.
#Then create class attributes with fixed values, which will be the available valid values:
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
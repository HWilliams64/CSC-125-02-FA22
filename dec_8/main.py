import random
from typing import Union
from fastapi import FastAPI

app = FastAPI()
COLORS = ("red", "green", "blue", "yellow", "black", "white", "gold", "silver", "purple")

@app.get("/")
def read_root():
    return {"message": "Hello world"}


@app.get("/random/number/{min_value}/{max_value}")
def read_root(min_value:int, max_value:int):
    return {"value": random.randint(min_value, max_value)}


@app.get("/random/color/")
def read_root():
    return {"value": random.choice(COLORS)}

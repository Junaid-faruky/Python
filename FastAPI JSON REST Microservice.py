from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

db = {}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    db[item_id] = item
    return {"id": item_id, "item": item}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return db.get(item_id, {"error": "not found"})

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False
items = []
@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/item", response_model=list[Item])
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item not found with id {item_id}")

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 5):
    return items[0:limit]

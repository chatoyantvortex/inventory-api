from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ---- SAMPLE MODEL ----
class Item(BaseModel):
    id: int
    name: str

# ---- ROOT ENDPOINT ----
@app.get("/")
def root():
    return {"message": "Inventory FastAPI is running!"}

# ---- SAMPLE POST ----
@app.post("/items")
def create_item(item: Item):
    return {"status": "success", "data": item}

# Import FastAPI
from fastapi import FastAPI

# create the app
app = FastAPI()

# Show this on main page ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Show item details when someone visits /items/any_number
@app.get("/items/{item_id}")
def read_items(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
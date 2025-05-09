# Import FastAPI
from fastapi import FastAPI

# create the app
app = FastAPI()

# Home page ("/")
@app.get("/")
def read_root():
    # return a simple message
    return {"message": "Hello, FastAPI!"}

# Show item details 
@app.get("/items/{item_id}")
def read_items(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
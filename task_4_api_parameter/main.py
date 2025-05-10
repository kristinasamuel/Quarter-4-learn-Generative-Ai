# API Parameters
# This project shows how to use API parameters in FastAPI.
from fastapi import FastAPI,Path,Query,Body
from pydantic import BaseModel

app = FastAPI()

# Define the data model for the item
class Item(BaseModel):
    name:str
    description:str | None = None  # Optional description
    price: float   # required field

#  GET request with a required path parameter
@app.get("/items/{item_id}")
async def read_item(
    item_id:int = Path(
        ...,   # ... parameter is required
        title = "The ID of the item",
        description = "A Unique identifier for the item",
        ge = 1
    )
):
    return {"item_id":item_id}

#  GET request with optional query parameters 
@app.get("items/")
async def read_items(
    q: str | None = Query(
        None, # optional query string
        title = "Query string",
        description = "Query string for searching items",
        min_length = 3,
        max_length = 50,
    ),
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, le=100)  
):
    return {
            "q": q,
            "skip": skip,
            "limit": limit,
            }

# PUT request with required path parameter, optional query parameter, and optional JSON body
@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),  # required path param
    q: str | None = Query(None, min_length=3),  # optional query
    item: Item | None = Body(None, description="Optional item data (JSON body)")  # optional JSON body
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})  # add query to result if provided
    if item:
        result.update({"item": item.model_dump()})  
    return result  


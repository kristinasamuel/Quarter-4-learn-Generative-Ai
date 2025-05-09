# Building a FastAPI Application with Complex Pydantic Models

# The code builds an API where users can send chat messages, and the bot replies.
# Metadata (timestamp + session ID) is auto-generated for each request.
# use FastAPI for routes and Pydantic for input/output data models.

from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel,Field
from datetime import datetime,UTC
from uuid import uuid4

# Initialize the FastAPI app with title, description, and version
app = FastAPI(
    title = "DACA Chatbot API",
    description = "A FastAPI-based API for a chatbot in the DACA tutorial series",
    version = "0.1.0",
)

# Define metadata model to store time and session info
class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda : datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))


# Define the structure of chat messages
class Message(BaseModel):
    user_id:str
    text:str
    metadata:Metadata 
    tags:list[str] | None = None  # Optional: any tags related to the message

#  Define the structure of the response that will be returned
class Response(BaseModel):
    user_id:str
    reply:str
    metadata:Metadata

# Home route (endpoint) Use GET method
@app.get("/")
async def root():
    return{
     "message": "Welcome to the DACA Chatbot API! Access /docs for the API documentation."
    }  

# Get user info by user_id (with optional role) GET request
@app.get("/users/{user_id}")
async def get_user(user_id:str , role:str | None = None):
    user_info = {
         "user_id": user_id,
        "role": role if role else "guest"  
    }
    return user_info

# Chat endpoint POST request (takes message and returns response)
@app.post("/chat/",response_model=Response)
async def chat(message:Message):
    if not message.text.strip():   # If user sends empty text
        raise HTTPException(
            status_code=400, detail="Message text cannot be empty")  # Return message
    reply_text = f"Hello, {message.user_id}! You said: '{message.text}'. How can I assist you today?"

    # Return a proper response model with generated metadata
    return Response(
        user_id = message.user_id,
        reply = reply_text,
        metadata = Metadata()   # Create new timestamp & session ID

    )    


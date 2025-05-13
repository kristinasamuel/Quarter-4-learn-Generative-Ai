# Task 6: Tracker Api
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from typing import Optional, Literal, Dict, List
from datetime import date

app = FastAPI()

# In-memory storage
Users: Dict[int, dict] = {}
Tasks: Dict[int, dict] = {}

user_id_counter = 1
task_id_counter = 1

# Models
class UserCreate(BaseModel):
    email: EmailStr
    username: constr(min_length=3, max_length=20)

# UserRead is used for returning user data
class UserRead(BaseModel):
    id: int
    email: EmailStr
    username: str

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    user_id: int
    
    # Validation to ensure due_date 
    @validator("due_date")
    def check_due_date(cls, value):
        if value <= date.today():
            raise ValueError("Due date must be in the future")
        return value 

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: date
    user_id: int
    status: str

class TaskStatus(BaseModel):
    status: Literal["pending", "in_progress", "completed"]


@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    data = {"id": user_id_counter, **user.dict()}
    Users[user_id_counter] = data
    user_id_counter += 1
    return data

@app.get("/users/{id}", response_model=UserRead)
def get_user(id: int):
    if id not in Users:
        raise HTTPException(404, "User not found")
    return Users[id]

@app.get("/users/{id}/tasks", response_model=List[Task])
def get_tasks_by_user(id: int):
    if id not in Users:
        raise HTTPException(404, "User not found")
    return [task for task in Tasks.values() if task["user_id"] == id]

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    if task.user_id not in Users:
        raise HTTPException(404, "User not found")

    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "due_date": task.due_date,
        "user_id": task.user_id,
        "status": "pending"
    }
    Tasks[task_id_counter] = new_task
    task_id_counter += 1
    return new_task

@app.get("/tasks/{id}", response_model=Task)
def get_task(id: int):
    if id not in Tasks:
        raise HTTPException(404, "Task not found")
    return Tasks[id]

@app.put("/tasks/{id}", response_model=Task)
def update_status(id: int, update: TaskStatus):
    if id not in Tasks:
        raise HTTPException(404, "Task not found")
    Tasks[id]["status"] = update.status
    return Tasks[id]
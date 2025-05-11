# Dependency Injection
# This project shows how to use Dependency Injection in FastAPI.

# 1.Simple Dependency Injection (No Parameters)

def get_simple_goal():
    return{"goal":"we are builidng AI A gents Workforce"}
@app.get("/get-simple-goal")    
def simple_goal(response:Annotated[dict, Depends(get_simple_goal)]):
    return response

# 2. Dependency with Parameter
# depency function
def get_goal(username:str):
    return {"gaol":"We are building AI Agents Workforce","username":username}

@app.get("/get-goal")
def get_my_goal(response: Annotated[dict,Depends(get_goal)]):
    return response

# 3. Dependency with Query Parameters
# This example shows how to use query parameters in a dependency function.
from fastapi import FastAPI,Depends,Query
from typing import Annotated

app:FastAPI = FastAPI()
# Dependency function
# This function checks the username and password from the query parameters.
def dep_login(username:str = Query(None),password : str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message" : "login Successfully...."}
    else:
        return {"message":"login failed......"}
    
@app.get("/signin")  
def login_api(user: Annotated[dict,Depends(dep_login)]):
    return user  

# 4. Multiple Dependencies
# This example shows how to use multiple dependencies in a single endpoint.
def depfunc1(num:int):
    num = int(num)
    num +=1
    return num

def depfunc2(num):
    num = int(num)
    num +=2
    return num

@app.get("/main/{num}")
def get_main(num:int,num1:Annotated[int,Depends(depfunc1)],num2:Annotated[int,Depends(depfunc2)]):
    total = num + num1 +num2
    return f"Total: {total}"

# 5. CLASSES
# This example shows how to use classes as dependencies.
blogs = {
    "1":"Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
    }

users = {
    "4":"Karan",
    "6":"Kristina"
}
class GetObjectOr404():
    def __init__(self,model)->None:
        self.model = model


    def __call__(self,id:str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj
    
blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name:Annotated[str,Depends(blog_dependency)]):
    return blog_name
    
user_dependency = GetObjectOr404(users)

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name

       


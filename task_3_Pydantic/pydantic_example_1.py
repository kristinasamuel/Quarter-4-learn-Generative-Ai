# Example 1: Basic Pydantic Model
 
# Import BaseModel to create a data model, and ValidationError to handle errors
from pydantic import BaseModel, ValidationError

# define a simple model
# Create a model (like a form structure) for a user
class User(BaseModel):
    id:int        # id  integer(1,2,3..)
    name:str      # name in string('Ali' , etc) 
    email:str     # email in string('abc@gmail.com)  
    age:int | None = None  # age is optional — can be a number or empty 

# create user data
user_data = {
    "id": 1,
    "name": "Kristina",
    "email": "Kristina@example.com",
    "age": 23
}

# Use the model to check and store the user data
user = User(**user_data)
# Print the user object
print(user)
#  Use model_dump() to convert the object to a dictionary
print(user.model_dump())

# try with wrong data to see what happens use try/except to catch errors
try:
    invalid_user = User(id="not_an_int",name ="Ali",email="ali@gmail.com")
except ValidationError as e:
    print(e)    

# output
# id=1 name='Kristina' email='Kristina@example.com' age=23
# {'id': 1, 'name': 'Kristina', 'email': 'Kristina@example.com', 'age': 23}
# 1 validation error for User
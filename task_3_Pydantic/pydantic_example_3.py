# Example 3. Custom Validators
# Add a custom validator to ensure the user’s name is at least 2 characters long:

# Import tools for model creation and validation
from pydantic import BaseModel,EmailStr,validator,ValidationError
from typing import List

# define the address model
class Address(BaseModel):
    street:str
    city:str
    zip_code:str

# Define the User model with validation
class UserWithAddress(BaseModel):
    id:int
    name:str
    email:EmailStr
    addresses:list[Address]

    # This function validates the name field
    @validator("name") 
    def name_must_be_at_least_2_characters(cls,v):
        if len(v) < 2:   
        # If name has less than 2 characters, show error
            raise ValueError("Name must be at least 2 characters long")
        return v
    
# Try to create a user with invalid name (only 1 letter)
try:
    invalid_user = UserWithAddress(
        id=104,
        name="A",
        email="kristina@gmail.com",
        addresses =[
      {"street": "b234 Main", "city": "karachi", "zip_code": "002341"}
        ],
    )

except ValidationError as e: 
    print(e)    # This will print the validation error message about the name

# Output
#  validation error for UserWithAddress
# name
#   Value error, Name must be at least 2 characters long [type=value_error, input_value='A']
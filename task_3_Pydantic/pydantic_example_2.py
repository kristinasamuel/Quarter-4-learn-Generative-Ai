# Example 2. Nested Models

from pydantic import BaseModel,EmailStr, ValidationError

# Define a nested model for Address
# Create a model for Address
class Address(BaseModel):
    street: str
    city:str
    zip_code:str

# Create a model for User that includes a list of addresses
class UserWithAddress(BaseModel):
    id:int
    name:str
    email:EmailStr
    addresses:list[Address]    # List of addresses

# Example data for one user with two addresses

user_data = {
    "id":101,
    "name":"Kristina",
    "email":"kristina@gmail.com",
    "addresses":[
                {"street": "A23 block", "city": "karachi", "zip_code": "10001"},
                {"street": "C12 block", "city": "karachi", "zip_code": "10001"},
    ],
}

# Validate and create the model 
user = UserWithAddress.model_validate(user_data)
# Print the model as a dictionary
print(user.model_dump())


# Output:
# {
    # 'id': 101,
    # 'name': 'Kristina',
    # 'email': 'kristina@gmail.com',
    # 'addresses':
    # [{'street': 'A23 block', 'city': 'karachi', 'zip_code': '10001'},
    # {'street': 'C12 block', 'city': 'karachi', 'zip_code': '10001'}]}

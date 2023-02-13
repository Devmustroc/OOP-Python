from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()  # Create an instance of the FastAPI class


class ProfileInfo(BaseModel):  # Create a class that inherits from the BaseModel class
    short_description: str
    long_description: str

class User(BaseModel):  # Create a class that inherits from the BaseModel class
    username: str  # The username is a string
    profile_info: ProfileInfo  # The profile_info is a ProfileInfo object
    liked_posts: Optional[list[int]] = None  #list[int]  # The liked_posts is a list of integers


def get_user_info() -> User:  # The function returns a User object
    profile_info = {"short_description": "test description", "long_description": "test long description"} # Create a dictionary
    profile_info = ProfileInfo(**profile_info)  # Create a ProfileInfo object
    user_content = {"username": "testuser", "profile_info": profile_info, "liked_posts": [1, 2, 3]}
    return User(**user_content)  # Return the User object



@app.get("/user/me",response_model=User) # The endpoint is /user/me and the response is a User object
def test_endpoint():  # The function returns a User object
    user = get_user_info()  # Call the get_user_info function
    return user # Return the User object

from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()  # Create an instance of the FastAPI class


class User(BaseModel):  # Create a class that inherits from the BaseModel class
    username: str  # The username is a string
    short_description: str = "default value"
    liked_posts: Optional[list[int]] = None  #list[int]  # The liked_posts is a list of integers


def get_user_info() -> User: # The function returns a User object
    content = {"username": "testuser", "short_description": "test description", "liked_posts": [1, 2, 3]}  # Create a dictionary
    return User(**content)  # Return the User object



@app.get("/user/me",response_model=User) # The endpoint is /user/me and the response is a User object
def test_endpoint():  # The function returns a User object
    user = get_user_info()  # Call the get_user_info function
    return user # Return the User object

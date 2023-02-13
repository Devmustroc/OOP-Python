from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()  # Create an instance of the FastAPI class


class User(BaseModel):  # Create a class that inherits from the BaseModel class
    username: str  # The username is a string
    short_description: str
    liked_posts:  list[int] #Optional[list[int]] = None


def get_user_info() -> User: # The function returns a User object
    content = {"username": "testuser","short_description": "My shor bio"} # Create a dictionary with the user information
    return User(**content)  # Return the User object



@app.get("/user/me",response_model=User) # The endpoint is /user/me and the response is a User object
def test_endpoint():  # The function returns a User object
    user = get_user_info()  # Call the get_user_info function
    return user # Return the User object

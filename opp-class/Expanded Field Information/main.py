from fastapi import FastAPI
#from typing import Optional
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()  # Create an instance of the FastAPI class


class User(BaseModel):  # Create a class that inherits from the BaseModel class
    username: str = Field(
        alias="name",
        title="The user's name",
        description="This is the user's name",
        min_length=1,
        max_length=50,
        default="user"
    )
    liked_posts: list[int] = Field(
        description="Array of integers",
        min_items=2,
        max_items=10,
    )  #list[int]  # The liked_posts is a list of integers


class FullUserProfilInfo(User):  # Create a class that inherits from the BaseModel class
    short_description: str
    long_description: str


def get_user_info() -> FullUserProfilInfo:  # The function returns a User object
    profile_info = {
        "short_description": "test description",
        "long_description": "test long description"
    }  # Create a dictionary
    user_content = {"profile_info": profile_info, "liked_posts": [1, 2, 3] * 2}  # Create a dictionary
    user = User(**user_content)  # Create a User object
    full_user_profile = {
        **profile_info,
        **user.dict()
    }
    print(full_user_profile)
    print(user)
    return FullUserProfilInfo(**full_user_profile)



@app.get("/user/me", response_model=FullUserProfilInfo)  # The endpoint is /user/me and the response is a User object
def test_endpoint():  # The function returns a User object
    full_user_profile = get_user_info()  # Call the get_user_info function
    return full_user_profile  # Return the User object

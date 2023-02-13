from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    short_description: str
    liked_posts: Optional[list[int]] = None


def get_user_info() -> User:
    content = {"username": "testuser","short_description": "My shor bio"}
    return User(**content)



@app.get("/user/me",response_model=User)
def test_endpoint():
    user = get_user_info()
    return user

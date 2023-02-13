from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    short_description: str
    liked_posts: list[int]


def get_user_info() -> (str, str):
    username = 'testuser'
    short_description = 'This is a test user'
    liked_posts = []
    return username, short_description, liked_posts


@app.get("/user/me",response_model=User)
def test_endpoint():
    username, short_description, liked_poste = get_user_info()
    user = User(username=username, short_description=short_description, liked_poste=liked_posts)
    return user

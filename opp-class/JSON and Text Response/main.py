from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.responses import JSONResponse

app = FastAPI()  # Create an instance of the FastAPI class

json_file = {"key1": 'hello', "key2": 2, "key3": {"kk1": "Nested", "kk2": 10}}


# @app.get("/test", response_class=PlainTextResponse)  # Create a route for the root path
@app.get("/test", response_class=JSONResponse)  # Create a route for the root path
def test_endpoint():  # Create a function to handle the request
    return json_file  # Return a string

@app.get("/test2", response_class=JSONResponse)  # Create a route for the root path
def test_endpoint2():  # Create a function to handle the request
    return json_file.get("key2")  # Return a string



@app.get("/", response_class=PlainTextResponse) # Create a route for the root path
#@app.get("/")  # Create a route for the root path
def home():  # Create a function to handle the request
    return "Welcome to the home page"  # Return a string

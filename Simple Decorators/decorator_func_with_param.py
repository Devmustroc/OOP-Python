import functools

user = {"username": "jose123", "access_level": "billing"}


def make_secure(func): # function that takes another function as an argument
    @functools.wraps(func)  # this is a decorator that will copy the name and docstring of the function that is passed as an argument
    def secure_function(*args, **kwargs): # inner function that is returned by the make_secure function
        if user["access_level"] == "admin":  # check if the user is an admin
            return func(*args, **kwargs) # return the function that was passed as an argument
        elif user["access_level"] == "billing":
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}." # return a message if the user is not an admin

    return secure_function  # return the inner function


@make_secure  # this is the same as get_admin_password = make_secure(get_admin_password)
def get_password(panel): # this is the same as secure_function()
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "Super Secure Password"

print(get_password("billing"))  # secure_function

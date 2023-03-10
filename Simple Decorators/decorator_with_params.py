import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(access_level):  # function
    def decorator(func):  # function that takes another function as an argument
        @functools.wraps(
            func)  # this is a decorator that will copy the name and docstring of the function that is passed as an argument
        def secure_function(*args, **kwargs):  # inner function that is returned by the make_secure function
            if user["access_level"] == access_level:  # check if the user is an admin
                return func(*args, **kwargs)  # return the function that was passed as an argument
            else:
                return f"No {access_level} permission for {user['username']}."  # return a message if the user is not an admin

        return secure_function  # return the inner function
    return decorator


@make_secure("admin")  # this is the same as get_admin_password = make_secure(get_admin_password)
def get_password(): # this is the same as secure_function()
    return "admin : 1234"



@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


print(get_password())  # secure_function
print(get_dashboard_password())

user = {"username": "anna", "access_level": "admin"}


print(get_password())  # secure_function
print(get_dashboard_password())
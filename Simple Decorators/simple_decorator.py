# user = {"username": "jose123", "access_level": "guest"}
#
#
# def get_admin_password():
#     return "1234"
#
#
# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permission for {user['username']}."
#     return secure_function
#
# get_admin_password = make_secure(get_admin_password)
# print(get_admin_password())

# secure_get_admin = make_secure(get_admin_password)


import functools

user = {"username": "jose123", "access_level": "guest"}


def make_secure(func): # function that takes another function as an argument
    @functools.wraps(func)  # this is a decorator that will copy the name and docstring of the function that is passed as an argument
    def secure_function(): # inner function that is returned by the make_secure function
        if user["access_level"] == "admin":  # check if the user is an admin
            return func() # return the function that was passed as an argument
        else:
            return f"No admin permission for {user['username']}." # return a message if the user is not an admin

    return secure_function  # return the inner function


@make_secure  # this is the same as get_admin_password = make_secure(get_admin_password)
def get_admin_password(): # this is the same as secure_function()
    return "1234"


print(get_admin_password.__name__)  # secure_function

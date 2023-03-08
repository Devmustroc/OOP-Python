# Arguments and Parameters

# def result(marks=None, name="None"):
#     if name and marks is None:
#         print(f'Hello {name}, your marks are not available')
#     else:
#         print(f'Hello {name}, your marks are {marks}')
#
# result(name="John", marks=None)  # using keyword arguments


# Arbitrary Arguments (*args)
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# def my_function(**kids):
#     young = 100
#     for kid in kids.values():
#         if kid < young:
#             young = kid
#     print(f'Hello {young}')
#
# child = {"Emil" : 50, "Tobias" : 30, "Linus" : 20}
# my_function(**child)


# def tup(*args):
#     for arg in args:
#         if arg == 0:
#             continue
#         print(arg, end=',')
# tup(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

def tup(n):
    for arg in n:
        if arg == 0:
            continue
        print(arg, end=',')

tup(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20) # error: tup() takes 1 positional argument but 20 were given
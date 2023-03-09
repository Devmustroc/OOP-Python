# unpacking arguments
#
# def add(x, y):
#     return x + y
#
# n , m = [1, 2]  # unpacking arguments list
# print(add(n, m))
# #
# dic1 = {'x': 1, 'y': 2}  # unpacking arguments dictionary
# print(add(x=dic1['x'], y=dic1['y']))
# print(add(**dic1))  # unpacking arguments dictionary

def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


# def apply(*args, operator):
#     if operator == '*':
#         return multiply(*args)
#     elif operator == '+':
#         return sum(args)
#     elif operator == '-':
#         return args[0] - sum(args[1:])  # subtracts all the other args from the first
#     else:
#         return 'No valid operator provided to apply()'
#
# ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(apply(*ls1, operator='/'))

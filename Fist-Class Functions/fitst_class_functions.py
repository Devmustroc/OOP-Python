# def devide(*dividend):
#     res = dividend[0]
#     try:
#         for value in dividend[1:]:
#             res /= value
#         return res
#     except ZeroDivisionError as err:
#         print(err)
#         return "You can't divide by zero"
#
# def multiply(*values):
#     res = 1
#     for value in values:
#         res *= value
#     return res
#
# def add(*values):
#     res = 0
#     for value in values:
#         res += value
#     return res
#
# def subtract(*values):
#     res = values[0]
#     for value in values[1:]:
#         res -= value
#     return res
#
#
# def calculate(*values, operator):
#     res = operator(*values)
#     if isinstance(res, float):
#         return f'{res:.2f}'
#     if isinstance(res, int):
#         return res
#     else:
#         return res
#
#
# choice = [devide, multiply, add, subtract]
#
# result = calculate(20, 4 , 3, 2, operator=choice[0])
# print(result)

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friend = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


def get_friend_name(friends):
    return friends["name"]

print(search(friend, "bob Smith", get_friend_name))
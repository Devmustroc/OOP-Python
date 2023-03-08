# Lambda Functions
# A lambda function is a small anonymous function.


# sub = lambda x, y: x - y
# print(sub(5, 3))
#
# # iteration in a lambda function
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list(map(lambda x: x * 2, lst))
# print(res)

# Creating a Duplicate List Elements Remover Function

# def remove_duplicates(lst):
#     unq = list(set(lst))
#     # return unq.sort() # error: 'NoneType' object is not subscriptable // because sort() returns None
#     unq.sort()
#     return unq
#
# lst = [55, 44, 33, 22, 11, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 100, 99, 88, 77, 66, 55, 44, 33, 22, 11]
# print(remove_duplicates(lst))

# Redefining the Built-In type( ) Function to Return the Type of an Object
#
# print(type(5))  # <class 'int'>
# print(type(5.0))  # <class 'float'>
# print(type('5'))  # <class 'str'>
#
# def dataType(obj):
#     return type(obj)
#
# print('\n')
#
# print(dataType(5))  # <class 'int'>
# print(dataType(5.0))  # <class 'float'>
# print(dataType('5'))  # <class 'str'>

# def dataType(obj):
#     dt = str(type(obj))
#     if 'str' in dt:
#         print('String')
#     elif 'int' in dt:
#         print('Integer')
#     elif 'float' in dt:
#         print('Float')
#     elif 'bool' in dt:
#         print('Boolean')
#     elif 'list' in dt:
#         print('List')
#     elif 'tuple' in dt:
#         print('Tuple')
#     elif 'set' in dt:
#         print('Set')
#     elif 'dict' in dt:
#         print('Dictionary')
#     else:
#         print('Unknown')
#
#
# dataType(5)  # Integer
# dataType(5.0)  # Float
# dataType('5')  # String
# dataType(True)  # Boolean
# dataType([1, 2, 3, 4, 5])  # List
# dataType((1, 2, 3, 4, 5))  # Tuple
# dataType({1, 2, 3, 4, 5})  # Set
# dataType({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})  # Dictionary
# dataType(None)  # Unknown


#Creating a Function to Smartly Round Decimal Points in a Result of Addition
#
# print(23.57 + 45.67)  # 69.24
# print(23.57 + 45.6705)  # 69.2405

def sum_r(*n):
    sm = 0
    lst = []
    for num in n:
        sm += num
        num = str(num).split('.')
        lst.append(len(num[1]))
    min_lst = min(lst)
    return round(sm, min_lst)

# print(sum_r(23, 45.6721, 45.7)) # index out of range: list index out of range // because 45.6721 has 5 decimal points
# print(sum_r(23.57, 45.67, 45.6705))  # 114.9
# print(sum_r(23.5, 45.67, 45.6705, 45.6705))  # 160.5

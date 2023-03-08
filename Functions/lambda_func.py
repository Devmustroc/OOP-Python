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

def remove_duplicates(lst):
    unq = list(set(lst))
    # return unq.sort() # error: 'NoneType' object is not subscriptable // because sort() returns None
    unq.sort()
    return unq

lst = [55, 44, 33, 22, 11, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 100, 99, 88, 77, 66, 55, 44, 33, 22, 11]
print(remove_duplicates(lst))
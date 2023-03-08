# Lambda Functions
# A lambda function is a small anonymous function.


# sub = lambda x, y: x - y
# print(sub(5, 3))

# iteration in a lambda function
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(map(lambda x: x * 2, lst))
print(res)
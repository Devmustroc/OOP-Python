# positional and keyword arguments

# def func(a, b, c): # a, b, c are positional arguments
#     print(a + b + c)
#
# func(1, 2, 3) # call function with positional arguments

# def substraction(a, b, c): # a, b, c are positional arguments
#     print(a - b - c)
#
# substraction() # error: missing 3 required positional arguments: 'a', 'b', and 'c'

def  result(name, marks):
        print (f'Hello {name}, your marks are {marks}')

result(name='John',marks=90) # using keyword arguments
result('John', 50) # positional arguments



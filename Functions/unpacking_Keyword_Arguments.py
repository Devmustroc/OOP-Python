# def named(**kwargs):
#     for key, value in kwargs.items():
#         x = str(value)
#         print(type(x))
#         return f'{key} = {x}'
#
#
# details = {'name': 'John', 'age': 30}
# print(named(**details)) # {'name': 'John', 'age': 30}

# def named(**kwargs):
#     print(kwargs)
#
#
# def print_nicely(**kwargs):
#     named(**kwargs)
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# print_nicely(name='Bob', age=25)

def both(*args, **kwargs):

    print(new)
    for key, value in kwargs.items():
        print(f'{key}: {value}', end='\n')

ls = [1, 3, 5]
dic1 = {'name': 'Bob', 'age': 25}
both(ls, dic1)
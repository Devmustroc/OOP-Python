# Arbitrary Keyword Arguments (**kwargs)
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# def info(**kw):
#     for key, value in kw.items():
#         print(f'{key} = {value}')
#
# # print all key-value pairs
# city = {'name': 'New York', 'state': 'NY', 'country': 'USA'}
# info(**city) # print all key-value pairs

# def pairVal(**kw):
#     for key, value in kw.items():
#         print(f'{key} = {value}')

# print all key-value pairs
# pairVal(name='John', age=30, city='New York') # print all key-value pairs
# pairVal() # print nothing without errors

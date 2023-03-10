# a = []
# b = a
#
# print(id(a))  # the same id as b / same adress in memory
# print(id(b)) # the same id as a /  same adress in memory
# print('\n')
# # but if we append a value to a
# a.append(21)
# print(a)  # [21] " the change is reflected in b"
# print(b)  # [21] " the change is reflected in a"
#
# print(id(a))  # the same id as b / same adress in memory
# print(id(b)) # the same id as a /  same adress in memory
# print('\n')
# # everything in python is an object and is stored in memory and is mutable
#
# a = ()
# b = ()
#
# a = a + (15, )
# print(a)  # (15, )
# print(b)  # ()
#
# print(id(a))  # different id from b / different adress in memory
# print(id(b)) # different id from a /  different adress in memory
# print('\n')
#
# a = 10
# b = 10
#
# print(id(a))  # the same id as b / same adress in memory
# print(id(b)) # the same id as a /  same adress in memory
# print('\n')
#
#
# a = 30
# b = 10
#
# print(id(a))  # different id from b / different adress in memory
# print(id(b)) # different id from a /  different adress in memory


a = "hello"
b = "hello"

print(id(a))  # the same id as b / same adress in memory
print(id(b)) # the same id as a /  same adress in memory

a += " world"

print(id(a))  # different id from b / different adress in memory
print(id(b)) # different id from a /  different adress in memory
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4ssword"),
    (3, "username", "1234")
]

user_mapping = {user[1] : user for user in users}
# print(user_mapping["Bob"])
# for user in users:
#     if user == user_mapping["Bob"]:
#         print(user)

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")
#
# _, username, password = user_mapping[username_input]
# # print(list(user_mapping[username_input]))
# if password_input == password:
#     print("Your details are correct!")
# else:
#     print("Your details are incorrect.")


# Create a variable called student_grades. This should be a dictionary with the following keys and values:
# 'name', 'grades', 'school'.
# the value of each mus be  'Jose', [70, 80, 90], 'Computing'

students = { 'name': 'Jose','school': 'Computing', 'grades': (66, 77, 88) }
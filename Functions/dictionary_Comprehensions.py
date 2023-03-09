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
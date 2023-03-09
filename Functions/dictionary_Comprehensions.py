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

students = {'name': 'Jose','school': 'Computing', 'grades': (66, 77, 88)}

#Assume the argument, data, is a dictionary.
# Modify the grades variable so that it accesses the 'grades' key of the data dictionary.

def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)

# Implement the function below
# Given a list of students (dicyonaies), calculate the average grade received on an exam, for the entire class.
# You must add all of the grades together
# You must also count how many students there are in total in the entier list

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])
    return total / count
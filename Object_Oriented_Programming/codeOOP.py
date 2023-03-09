class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def average_grade(self, students):
        total = 0
        count = 0
        for student in students:
            total += student.get_grade()
            count += 1
        return total / count


s1 = Students('Bob', 19, 95)
print(s1.get_grade(), s1.get_name())
from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):  # this is
        self.name = name
        self.grades = grades or []  # this is the same as: if grades is None: self.grades = [] else: self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)





student = Student("Rolf")
student2 = Student("Bob")
student.take_exam(90)
print(student.grades)
print(student2.grades)

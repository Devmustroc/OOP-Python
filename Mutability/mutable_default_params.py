from typing import List

class Student:
    def __ini__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
bob.take_exam(90)
bob.take_exam(80)
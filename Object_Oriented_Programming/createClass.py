# class Coder():
#     def __init__(self, name, age, language):
#         self.name = name
#         self.age = age
#         self.language = language
#
# cd = Coder("jhon", 30, 'Python')
# print(cd.name, cd.age, cd.language)

class Coder():
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def info(self):
        print(f'Hello {self.name}, your age is {self.age} and you know {", ".join(self.language)}')

cd = Coder("jhon", 30, 'Python')
cd.info()

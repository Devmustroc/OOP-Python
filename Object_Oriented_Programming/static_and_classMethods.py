class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    # def __str__(self):
    #     return f'ClassTest instance {self}'

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")
    @staticmethod
    def static_method():
        print("Called static_method.")


test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
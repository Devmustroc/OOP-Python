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


test = ClassTest()  # create an instance of ClassTest
test.instance_method() # instance method takes the object as the first argument
ClassTest.class_method() # class method takes the class as the first argument
ClassTest.instance_method(test) # instance method takes the object as the first argument
ClassTest.static_method()  # static method doesn't take any arguments
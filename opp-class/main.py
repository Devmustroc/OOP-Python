class Animal:
    fiends = []
    def __init__(self, name, age, height, weight, health, color):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.health = health
        self.color = color

    def print_name(self):
        print(f"This animal's name is: {self.name}\n"
              f"This animal's height is: {self.height}\n"
              f"This animal's weight is: {self.weight}\n"
              f"This animal's height is: {self.health}\n"
              f"This animal's height is: {self.color}\n")

    def print_age(self):
        print(f"This animal's age is: {self.age}")

    def print_color(self):
        print(f"This animal's color is: {self.color}")

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)


class Dog(Animal):
    def __init__(self, name, age, height, weight, health, color, breed, owner):
        super().__init__(name, age, height, weight, health, color)
        self.breed = breed
        self.owner = owner

    def print_breed(self):
        print(f"This dog's breed is: {self.breed}")

    def print_owner(self):
        print(f"This dog's owner is: {self.owner}")

    def print_name(self):
        print(f"This dog's name is: {self.name}")

    @classmethod
    def greet(self):
        print("Woof Woof")


littleDog = Dog("Little Dog", 2, 0.5, 5, "good", "black", "Pitbull", "John")
littleDog.print_name()
littleDog.print_age()
littleDog.print_color()
littleDog.print_breed()
littleDog.print_owner()
print(littleDog.calculate_bmi())

Dog.greet()

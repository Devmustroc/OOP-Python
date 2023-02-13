class Animal:
    def __init__(self, name, age, height, weight, health, color):
        self.name = name,
        self.age = age,
        self.height = height,
        self.weight = weight,
        self.health = health,
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



animal1 = Animal("Dog", 5, 3, 10, 100, "black")
animal1.print_name()

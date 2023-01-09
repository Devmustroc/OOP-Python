# Class Constructor/Initialize (__init__& self)

class Car:
    # Class Attributes / Variables
    no_of_tires = 4

    # Class Constructor/initialize ( Method with a special name)
    def __init__(self, make, model, year, color, moon_roof=False):
        # Object Attributes / Variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.moon_roof = moon_roof
        self.engine_running = False

    # Methods
    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False

    # destructor
    def __del__(self):
        print(f"{self.make} {self.model}: Destructor Invoked!")


def main():
    car1 = Car("Ford", "Mustang", 2022, "Blue")
    car2 = Car("Tesla", "model S", 2022, "red", True)

    print(" Details OF YOUR CAR ".center(50, '#'))
    print(f"Make: {car1.make}".upper())
    print(f"Model: {car1.model}")
    print(f"Year: {car1.year}")
    print(f"Color: {car1.color}")
    print(f"Moon Roof: {car1.moon_roof}")
    print(" Details Number 2 ".center(50, "-"))
    print(f"Make: {car2.make}".upper())
    print(f"Model: {car2.model}")
    print(f"Year: {car2.year}")
    print(f"Color: {car2.color}")
    print(f"Moon Roof: {car2.moon_roof}")
    # Class Attributes:
    print(" Class Attributes : ".center(50, "#"))
    print(f"Car1: {car1.no_of_tires}")
    print(f"Car1: {car2.no_of_tires}")
    print(f"Car: {Car.no_of_tires}")

    # Delete
    print(f"Deleting Object")
    del car2
    del car1


if __name__ == '__main__':
    main()

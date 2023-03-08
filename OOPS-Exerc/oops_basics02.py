# Class Constructor/Initialize (__init__& self)

class Car:
    # Class Attributes / Variables
    no_of_tires = 4

    # Class Constructor/initialize ( Method with a special name)
    def __init__(self):
        # Object Attributes / Variables
        self.make = ""
        self.model = ""
        self.year = ""
        self.color = ""
        self.moon_roof = ""
        self.engine_running = ""

    # Methods
    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False


def main():
    car1 = Car()
    car2 = Car()

    # Assigne Values
    car1.make = "Tesla"
    car1.model = "Model X"
    car1.year = 2022
    car1.color = "Purple"
    car1.moon_roof = False

    print(" Details OF YOUR CAR ".center(50, '#'))
    print(f"Make: {car1.make}".upper())
    print(f"Model: {car1.model}")
    print(f"Year: {car1.year}")
    print(f"Color: {car1.color}")
    print(f"Moon Roof: {car1.moon_roof}")

    # Class Attributes:
    print(" Class Attributes : ".center(50, "#"))
    Car.no_of_tires = 25
    print(f"Car1: {car1.no_of_tires}")
    print(f"Car: {Car.no_of_tires}")
    print(f"Cars 1 : {car1.no_of_tires}")
    print(f"Car2 : {car2.no_of_tires}")


if __name__ == '__main__':
    main()

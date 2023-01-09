# Using Methods

class My_calc:
    # class constructor initializer (Method with a special name)

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def total(self):
        return self.num1 + self.num2

    def diff(self):
        return self.num1 - self.num2


def main():
    print(f"hello from the main() Method")
    calc1 = My_calc(5, 50)
    sum = calc1.total()
    diff1 = calc1.diff()

    print(f"Total 1 : {sum}")
    print(f"Difference 1 : {diff1}")

    calc2 = My_calc(60, 33)
    sum2 = calc2.total()
    diff2 = calc2.diff()

    print(f"Total 2 : {sum2}")
    print(f"Difference 2 : {diff2}")

if __name__ == "__main__":
    main()

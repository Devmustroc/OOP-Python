# Public & private Access Modifiers
# Public

class Employee:

    # Class Constructor (Method with a special name)
    def __init__(self, first_name, last_name, base_annual_salary, bonus_percentage):
        self.first_name = first_name
        self.last_name = last_name
        self.base_annual_salary = base_annual_salary
        self.bonus_percentage = bonus_percentage

    # Methods
    def get_monthly_gross(self):
        return self.base_annual_salary / 12

    def get_standard_annual_bonus_amount(self):
        return self.base_annual_salary * (self.bonus_percentage / 100)


def main():
    print("hello from main()")

    employee1 = Employee('Nabil', 'heryouli', 10000.00, 5)
    monthly_gross_pay = employee1.get_monthly_gross()
    standard_annual_bonus = employee1.get_standard_annual_bonus_amount()
    print(f"First Name: {employee1.first_name}")
    print(f"Last name: {employee1.last_name}")
    print(f'Annual Salary : {employee1.base_annual_salary:.2f}')
    print(f"Monthly gross salary : {monthly_gross_pay}")
    print(f"Annual Standad Bonus: {standard_annual_bonus}")


if __name__ == '__main__':
    main()

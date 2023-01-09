# Public & private Access Modifiers
# Public

class Employee:

    # Class Constructor (Method with a special name)
    def __init__(self, first_name, last_name,):
        self.first_name = first_name
        self.last_name = last_name
        self.__base_annual_salary = 0
        self.__bonus_percentage = 0
        self.__holiday_week = 0

    # Methods
    def get_monthly_gross(self):
        return self.__base_annual_salary / 12

    def get_standard_annual_bonus_amount(self):
        return self.__base_annual_salary * (self.__bonus_percentage / 100)

    # Getters
    @property
    def holiday_week(self):
        return self.__holiday_week

    @property
    def base_annual_salary(self):
        return self.__base_annual_salary

    @property
    def bonus_percentage(self):
        return self.__bonus_percentage

    # Setter
    @holiday_week.setter
    def holiday_week(self, holiday_week):
        if 1 <= holiday_week <= 8:
            self.__holiday_week = holiday_week
        else:
            print(f"Holiday week must be between 50 and 90")

    @base_annual_salary.setter
    def base_annual_salary(self, base_annual_salary):
        if 45000.00 <= base_annual_salary <= 120000.00:
            self.__base_annual_salary = base_annual_salary
        else:
            print(f"Annual base salary must be between 45k and 120k!")

    @bonus_percentage.setter
    def bonus_percentage(self, bonus_percentage):
        if 0.05 <= bonus_percentage <= .21:
            self.__bonus_percentage = bonus_percentage
        else:
            print(f"percentage must be between 5% (0.5) and 21% (0.21)")

def main():
    employee1 = Employee('Must', "Rowk")
    employee1.bonus_percentage = 0.51
    employee1.base_annual_salary = 45000.00
    employee1.holiday_week = 5
    monthy_gross_pay = employee1.get_monthly_gross()
    standard_annual_bonus = employee1.get_standard_annual_bonus_amount()

    print(f"Annual Salary : {employee1.base_annual_salary:.2f}")
    print(f"Holiday Week is : {employee1.holiday_week}")
    print(f"Monthly Gross Salary : {monthy_gross_pay}")
    print(f"Annual Standart Bonus : {standard_annual_bonus}")


if __name__ == '__main__':
    main()

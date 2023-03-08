# Public & private Access Modifiers
# Public

from oops_getting_deeper_private import Employee

employee1 = Employee('Karim', 'Newyork', 300000.00)
employee1.__bonus_percentage = 25
monthly_gross_pay = employee1.get_monthly_gross()
standard_annual_bonus = employee1.get_standard_annual_bonus_amount()
emp_id = employee1.get_emp_id()
print(f"{emp_id} : ID OF : {employee1.first_name}")
print(f"First Name: {employee1.first_name}")
print(f"Last name: {employee1.last_name}")
print(f'Annual Salary : {employee1.base_annual_salary:.2f}')
print(f"Monthly gross salary : {monthly_gross_pay}")
print(f"Annual Standard Bonus: {standard_annual_bonus}")
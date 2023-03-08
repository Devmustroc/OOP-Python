# Public & private Access Modifiers
# Public


from oops_getting_deeper_client_salary import Employee

employee1 = Employee('Nabil', 'heryouli', 500000.00, 5)
monthly_gross_pay = employee1.get_monthly_gross()
standard_annual_bonus = employee1.get_standard_annual_bonus_amount()
print(f"First Name: {employee1.first_name}")
print(f"Last name: {employee1.last_name}")
print(f'Annual Salary : {employee1.base_annual_salary:.2f}')
print(f"Monthly gross salary : {monthly_gross_pay:.2f}")
print(f"Annual Standad Bonus: {standard_annual_bonus:.2f}")
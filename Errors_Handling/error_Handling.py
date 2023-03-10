def devide(dividend, divisor):
    try:
        return dividend/divisor
    except ZeroDivisionError as err:
        print(err)
        return "You can't divide by zero"


grade = []
average = devide(sum(grade), len(grade))
print(f"this is {average}")

#Return Values from User-Defined Functions Using the Return Keyword
# To let a function return a value, use the return statement:

def add(*n):
    sum = 0
    for num in n:
        sum += num
    return sum

sum = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sum)
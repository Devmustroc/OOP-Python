# import

from callMethod import My_calc

calc1 = My_calc(100, 50)
sum = calc1.total()
diff1 = calc1.diff()

print(f"Total 1 : {sum}")
print(f"Difference 1 : {diff1}")

calc2 = My_calc(50, 25)
sum2 = calc2.total()
diff2 = calc2.diff()

print(f"Total 2 : {sum2}")
print(f"Difference 2 : {diff2}")

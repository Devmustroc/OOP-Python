# for e in 'python': // string
#     print(e)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   // list of integers
# for e in lst:
#     print(e * 2)


# lst = ["python", "Java", "C#", "C++", "C", "Ruby", "Perl", "PHP", "JavaScript"]
# for e in lst:
#     if e == "C":
#         print(e.lower())
#     if e == "C++":
#         lst.append("Go")
#     if e == len(lst):
#         break
#     print(e.upper())

# for num in range(10, 2, -2):  # range(start, stop, step) // 10, 8, 6, 4
#     print(num)

# for num in range(1, 11):
#     for i in range(1, 11):
#         res = num * i
#         print(f'{num} * {i} = {res}')
#     print('\n')

# lst = [9, 4, 3, 4, 5, 6, 1, 8, 9, 10,2,4,3,5,11,15]
# unq = []
# for e in lst:
#     if e not in unq and e < 10:
#         unq.append(e)
# print(lst)
# print(unq)

lst = [9, 4, 3, 4, 5, 6, 1, 8, 9, 10,2,4,3,5,11,15]
unq = [set(lst)]
for e in unq:
    if e < 10:
        unq.append(e)
print(lst)
print(unq)
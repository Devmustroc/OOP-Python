# for e in 'python': // string
#     print(e)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   // list of integers
# for e in lst:
#     print(e * 2)


lst = ["python", "Java", "C#", "C++", "C", "Ruby", "Perl", "PHP", "JavaScript"]
for e in lst:
    if e == "C":
        print(e.lower())
    if e == "C++":
        lst.append("Go")
    if e == len(lst):
        break
    print(e.upper())
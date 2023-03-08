# Arguments and Parameters

def result(marks=None, name="None"):
    if name and marks is None:
        print(f'Hello {name}, your marks are not available')
    else:
        print(f'Hello {name}, your marks are {marks}')

result(name="John", marks=None)  # using keyword arguments

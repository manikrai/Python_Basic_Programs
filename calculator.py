def getInput():
    f_num = int(input("Enter first number: "))
    a_num = int(input("Enter Second number: "))
    return f_num, a_num


def add():
    x, y = getInput()
    return x + y


def sub():
    x, y = getInput()
    return x - y


def div():
    x, y = getInput()
    return x // y


def mul():
    x, y = getInput()
    return x * y


def errorHandler():
    return "Invalid Choice"


print('''
     1. Add
     2. Sub
     3. Div
     4. Mul
''')

choice = int(input("Enter your choice: "))

# operations = [add, sub, div, mul]
# output = operations[choice - 1]()
# print(output)
''' now I'll perform this operation using dictionary '''

operations = {
    1: add,
    2: sub,
    3: div,
    4: mul
}

output = operations.get(choice, errorHandler)()

print(output)

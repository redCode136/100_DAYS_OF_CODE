def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = float(input("please enter first number: "))
num2 = float(input("please enter second number: "))

for symbles in operations:
    print(symbles)

operation_symbles = input("Please choose operation from line above: ")
operation_function = operations[operation_symbles](num1, num2)
answers = operation_function

print(f"{num1} {operation_symbles} {num2} = {answers}")

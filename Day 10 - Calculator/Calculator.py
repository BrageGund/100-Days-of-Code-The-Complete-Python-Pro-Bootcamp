import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calc():
    loop = True
    num1 = float(input("What is your first number: "))

    while loop:
        for sym in operations:
            print(sym)
        operator = input("Pick an operator: ")
        num2 = float(input("what is your last number: "))

        Answer = operations[operator](num1,num2)
        print(f"{num1} {operator} {num2} = {Answer}")

        decision = input(f"press 'y' to calculating with {Answer}, or 'n' to start over: ")

        if decision == "y":
            num1 = Answer
        else:
            loop = False
            print(20*"\n")
            calc()
calc()

# First = float(input("What is your first number: "))
# loop = True
# while loop:
#     print("+\n-\n*\n/")
#     operator = input("Pick an operator: ")
#     Last = float(input("What is your first number: "))
#
#     if operator == "+":
#         result = add(First, Last)
#         print(f"The answer is: {result}")
#
#     elif operator == "-":
#         result = subtract(First, Last)
#         print(f"The answer is: {result}")
#
#     elif operator == "*":
#         result = multiply(First, Last)
#         print(f"The answer is: {result}")
#
#     elif operator == "/":
#         result = divide(First, Last)
#         print(f"The answer is: {result}")
#     else:
#         print("invalid operator")
#
#     decision = input(f"press 'y' to calculating with {result}, and 'n' to stop: ")
#
#     if decision == "y":
#         First = result
#     elif decision == "n":
#         loop = False
#     else:
#         print("invalid choice")


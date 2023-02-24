from art import logo
# Calculator Operation Functions

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Operations Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Calculator
def calculator():

    # printing logo
    print(logo)

    # first number
    num1 = float(input("First Number: "))

    # while continue_calculation is true, keep calculating with the result of previous calculation
    continue_calculation = True

    while continue_calculation:
        # printing keys from operations dictionary
        for symbol in operations:
            print(symbol)

        # ask user to input which operation to perform
        operation_symbol = input("Pick an operation from above: ")

        # second number
        num2 = float(input("Second Number: "))

        # using keys of operations dictionary to determine which calculator operation function to call
        calculation_function = operations[operation_symbol]

        # result of calculation
        answer = calculation_function(num1, num2)

        # printing the result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # asking the user if they want to continue calculating with the result
        should_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n to exit: "
        )
        # if no, then stop while loop, and recursively call calculator function to start a new calculation
        if should_continue == 'n':
            continue_calculation = False
            calculator()
        # if yes, use the result as num1 and re-loop
        elif should_continue == 'y':
            num1 = answer

# call calculator when hit run
calculator()
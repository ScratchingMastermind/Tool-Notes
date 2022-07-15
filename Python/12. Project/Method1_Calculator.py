# Build a calculator with all the basic arithmetic functions. Bonus points for additional functions

def addition(num1, num2):
    result = num1+num2
    print(result)
    return


def subtraction(num1, num2):
    result = num1-num2
    print(result)
    return


def division(num1, num2):
    result = num1/num2
    print(result)
    return


def multiplication(num1, num2):
    result = num1*num2
    print(result)
    return


def main():
    print("Calc V2 by Scratching Mastermind")
    num1 = float(input("Insert the first number: "))
    op = input("Insert the operation: ")
    num2 = float(input("Insert the second number: "))
    if op == "+":
        addition(num1, num2)
    if op == "-":
        subtraction(num1, num2)
    if op == "/":
        division(num1, num2)
    if op == "*":
        multiplication(num1, num2)
    return


main()

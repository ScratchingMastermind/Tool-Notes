# Build a calculator with all the basic arithmetic functions.

print("Calc V2 by Scratching Mastermind")
num1 = float(input("Insert the first number: "))
op = input("Insert the operation: ")
num2 = float(input("Insert the second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)

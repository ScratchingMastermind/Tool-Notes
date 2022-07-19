'''Used when you want to stop errors from breaking your program. 
When errors occurs you designated an desired output to the user
'''

'''
This program works as long as the number is an integer and not float or string. We get:
number = int(input("enter a number: "))
ValueError: invalid literal for int() with base 10: '5.2'
'''
number = int(input("enter a number: "))
print(number5)

catching that error

try:
    number = int(input("enter a number: "))
    print(number5)
except:
    print(("Invalid Input. Not an integer"))

# You can also specify which type of error you are trying to catch. For example ValueError and ZeroDivisionError

try:
    #value = 4/0
    number = int(input("enter a number: "))
    print(number5)
except ValueError:
    print("Invalid Input. Not an integer")
except ZeroDivisionError:
    print("Divide by zero")

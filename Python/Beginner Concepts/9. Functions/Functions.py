# Functions are basically a collection of code that do a specific thing

def greeting():  # function definition
    print("Hello")


greeting()  # function calling - it runs whatever is inside the function

# You can also pass parameter to the function


def greeting1(name, age, gender):  # function definition

    print("Hello "+name)
    print("You are " + str(age) + " and " + gender)


# function calling - it runs whatever is inside the function
greeting1("Mastermind", 35, "Male")
greeting1("Mastermind", "35", "Male")  # same output 'cause str() conversion.

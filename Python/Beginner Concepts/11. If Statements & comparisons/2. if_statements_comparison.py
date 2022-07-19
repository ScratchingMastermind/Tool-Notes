# 1. Create a function with 3 parameters that spits out the highest number you give it to using if statements.
# 2. Do the same without if statements.

def comparator(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num1 and num2 >= num3:
        print(num2)
    else:
        print(num3)
    return


comparator(60, 50, 80)
print("Improvements")


def comparator(num1, num2, num3):
    number = [num1, num2, num3]
    max_num = max(number)
    min_num = min(number)
    print("Max:" + str(max_num) + "\nMin: " + str(min_num))
    return


comparator(8, 100, 53)

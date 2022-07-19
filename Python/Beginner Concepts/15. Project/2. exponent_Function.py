# Create a function that computes exponents. for example 2^2 = 4 using for loop


def exponent(base, exponent):
    result = 1
    for number in range(exponent):
        result = result * base
    return print(result)


exponent(2, 2)

# when executing condition where true or false implies, or comparison you can use if statements.

is_male = True
is_tall = True

print("Example - 1")

if is_male:
    print("Yes are a male")
else:
    print("You are not a male")

print("Example - 2")
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are not male or tall")

# Usefully operator are
# and
# or

is_male = False
is_tall = True
print("Example - 3")
if is_male and is_tall:
    print("You are a tall male")
elif not(is_male) and is_tall:
    print("You are a tall female")
else:
    print("You are not male or tall")

# Working with Strings

# Creating a new line in the string

print("Today's Breakfast was awesome.\nBut Dinner not so much.")

# Inserting especial characters you have to escape it with \

print('Who\'s there?')

# String Variable
name = "Rose"
print(name)

# concatenation - is the operation of joining character strings end-to-end

print(name + " is Cool")

# Using Functions with the Strings

print(name.upper())
print(name.isupper())         # checking if it is UPPERCASE - False
print(name.upper().isupper())  # Converts to uppercase - True
print(len(name))              # checking string length
print(name[0])                # getting individual character inside a string
print(name.index("R"))        # Passing Parameters. Position of the character


print(name.replace("Rose", "Merry"))

# A list is essentially a structure to store a bunch of data in list form
# Unlike a variable a list can store 1 or more values inside the same object.

names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
print(names)

# You can also refer to a particular name using indexes
# You can also start from the right to left by using "-1". -1 being the first value from right to left.
print(names[2])

# You also extract a range of values

print(names[1:])     # Print everything from the second position
print(names[1:3])    # prints from 2nd to 3rd but no included

# You can do modify characters

print(names[2].replace("Carlos", "Yo"))  # Yield same resorts
names[2] = "G"  # index position 2
print(names[2])  # prints the changed Character

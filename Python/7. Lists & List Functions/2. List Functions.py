names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
numbers = [34, 4823, 53, 32, 54, 3434, 3, 34, 32]
print(names)

# Extend function - appending one list to another
names.extend(numbers)
print(names)

# Add individual elements to another list
names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
names.append("Rio")
print(names)

# Add to desired location
names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
names.insert(3, "Rio")  # takes two parameters index and object
print(names)

# Removing values
names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
names.remove("Tom")
print(names)

# removing the last element using pop
names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
names.pop()  # takes integer to justify position
print(names)

# Reset the list aka erase
names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
names.clear()
print(names)

# Checking if certain value exists
# names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
# print(names.index("Dias"))  # shows position of the character
# print(names.index("Berlin"))

# Count the number of similar elements
names = ["Gerald", "Dias", "Carlos", "Carlos", "River", "Obi", "Tom"]
print(names.count("Carlos"))

# Sorting the list
names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
numbers = [34, 4823, 53, 32, 54, 3434, 3, 34, 32]
names.sort()
numbers.sort()
print(names)
print(numbers)

# Reverse the order
names = ["Gerald", "Dias", "Carlos", "River", "Obi", "Tom"]
numbers = [34, 4823, 53, 32, 54, 3434, 3, 34, 32]
names.reverse()
numbers.reverse()
print(names)
print(numbers)

# Copy

Names1 = names.copy()
print(Names1)

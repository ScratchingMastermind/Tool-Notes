# Nested list - an list which a list
number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Nested for loops
# to access number_grid[index of the sets-of-numbers][index of the item within the set])
print(number_grid[0][2])  # prints 3

for sets in number_grid:
    for numbers in sets:
        print(numbers)

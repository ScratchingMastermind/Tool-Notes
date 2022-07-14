# Similar to a list but you can't modify its content like a list.
# You can think of it has points in a cartesian plane, where xyz represent
# a single point and if changed represent a totally different location.

coordinates = (3, 4, 5)
print(coordinates[1])  # elements inside a tuple are also indexed

# You can also create a list of tuples
coordinates_list = [(3, 4, 5), (5, 3, 5), (45, 67, 34)]
print(coordinates_list[1])

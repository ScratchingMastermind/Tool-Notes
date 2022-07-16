# looping through a different collection of item. Ex: an array/list, loop through the letter of a string.
# for [variable 1] in [variable 2].
# Variable 1 changes in every iteration of the loop
# Variable 2 is the collection of values you want too loop over.

collection = "Mastermind"
for letter in collection:
    print(letter)


friends = ["Mastermind", "Carlos", "John", "Daikon"]
for friend in friends:
    print(friend)

# You can also use range to loop through an array
for friend in range(len(friends)):
    print(friends[friend])

# # you can also use numbers
# for numbers in range(10):
#     print(numbers)
# # Range of numbers
# for numbers in range(3, 10):
#     print(numbers)

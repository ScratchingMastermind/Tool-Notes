# open(file_location,mode)
'''
Modes
r - read the files
w - write to the file
a - append to the file
r+ - read and write to the

read() -> reads the whole file
readline() -> reads the first line
readlines() -> put the lines in an array, that can be called by its index
readlines()[1]
read
'''
note = open(
    "E:/Projects/GitHub/Repositories/Tool-Notes/Python/19. Reading Files/test.txt", "r")
print(note.readlines()[1])  # reads second line
note.close()

# We cam also use for loops to read the lines of text

for names in note.readlines():
    print(names)
note.close()

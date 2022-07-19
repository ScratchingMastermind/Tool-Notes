# adding a new name - append to the file
note = open(
    "E:/Projects/GitHub/Repositories/Tool-Notes/Python/19. Files handling/test.txt", "a")
note.write("\nocean")  # reads second line
note.close()

# Writing a hole new file - Overrides everything on the existing file

note = open(
    "E:/Projects/GitHub/Repositories/Tool-Notes/Python/19. Files handling/test1.txt", "w")
note.write("ocean")  # reads second line
note.close()

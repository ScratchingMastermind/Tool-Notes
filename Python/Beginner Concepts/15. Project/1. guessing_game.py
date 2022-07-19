# Create a guessing/riddle game with things learned so far, where the user has unlimited guesses to a guess word(password).

secret_word = "towel"
guess = ""

print("Riddle Me This")
print("What gets wet while drying?")
while guess != secret_word:
    guess = input("Enter your guess: ")
    if guess == secret_word:
        print("Thats correct. You Win")
    elif guess != secret_word:
        print("Try again.")


# Improvement. keep track of the guess, and Display it if possible.

secret_word = "towel"
guess = ""
display_tries = 1


print("Riddle Me This. You have 3 attempts")
print("What gets wet while drying?")
while guess != secret_word and display_tries != 4:
    if display_tries < 4:
        print("Attempt: " + str(display_tries))
        display_tries += 1
        guess = input("Enter your guess: ")
        if guess == secret_word:
            print("Correct!")
        elif guess != secret_word:
            print("Try again.")

if display_tries == 4:
    print("Out of Attempts")
else:
    print("You win!")

# Improvement 2. keep track of the guess, and Display it if possible.

secret_word = "towel"
guess = ""
display_tries = 1
guess_count = 0
guess_limit = 3

print("Riddle Me This. You have 3 attempts")
print("What gets wet while drying?")

while guess != secret_word and display_tries != 4:
    if guess_count < guess_limit:
        print("Attempt: " + str(display_tries))
        display_tries += 1
        guess_count = +1
        guess = input("Enter your guess: ")

if display_tries == 4:
    print("Out of Attempts")
else:
    print("Correct\nYou win!")

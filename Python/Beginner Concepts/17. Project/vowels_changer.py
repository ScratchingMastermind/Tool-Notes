'''
change the vowel of any given words to P
----------------------------------------
dog -> dPg
computer -> cPmpPtPr
'''


def vowel_changer(word):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    final = ""
    for letter in word:
        # print(letter)
        if letter in vowel:
            final += "P"
        else:
            final += letter
    return print(final)


vowel_changer(input("Enter the desired word: "))

# Improvement 1


def vowel_changer(word):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    final = ""
    for letter in word:
        # print(letter)
        if letter in vowel:
            if letter.isupper():
                final += "P"
            else:
                final += "p"
        else:
            final += letter
    return print(final)


vowel_changer(input("Enter the desired word: "))

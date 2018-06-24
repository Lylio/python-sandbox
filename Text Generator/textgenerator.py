import random, string


vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = string.ascii_lowercase

letter_input_1 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")
letter_input_2 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")
letter_input_3 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")

def generator():
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonants)
    else:
        letter1 = random.choice(letters)

    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonants)
    else:
        letter2 = random.choice(letters)

    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter3 = random.choice(consonants)
    else:
        letter3 = random.choice(letters)

    name = letter1+letter2+letter3
    return (name)


for i in range(10):
    print(generator())


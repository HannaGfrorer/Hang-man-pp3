import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word:").upper()
        

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
        if len(guess) == 1 and guess.isalpha()
           if guess in guessed_letters:
              print("you already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word") 
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list =list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess_isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_comletion = word
        else:
            print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")

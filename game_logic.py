import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        display_word += (letter + " ") if letter in guessed_letters else "_ "
    print("Word: ", display_word)
    print()

def is_word_guessed(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes and not is_word_guessed(secret_word, guessed_letters):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1

    display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("You saved the snowman! The word was:", secret_word)
    else:
        print("Game Over! The word was:", secret_word)

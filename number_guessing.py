# number_guessing.py

import random

def generate_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

def check_guess(secret_number, guess):
    """Checks the guess and provides feedback."""
    if guess < secret_number:
        return "Too low! Try again."
    elif guess > secret_number:
        return "Too high! Try again."
    else:
        return "Congratulations! You guessed the number!"

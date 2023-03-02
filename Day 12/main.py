# imports
from art import logo
from random import randint
from os import system

# global initialization
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

'''Asks the user how difficult do they want the game to be and sets number of attempts accordingly.'''
def set_difficulty():
    # Asks the user to choose the level of difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # If easy, attempts = 10
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    # If hard, attempts = 5
    elif difficulty == "hard":
         return HARD_LEVEL_ATTEMPTS

'''Asks the user to guess and number and compares with the result while there are still attempts left.'''
def guess_the_number():
    # prints logo
    print(logo)

    # greeting
    print("Welcome to the Number Guessing Game!")

    # using randint from random module to select a random number between 1 and 100
    chosen_number = randint(1, 100)

    print("I'm thinking of a number between 1 and 100.")

    attempts_remaining = set_difficulty()    

    game_over = False

    while not game_over:

        # printing number of attempts left after every guess
        print(
            f"You have {attempts_remaining} attempts remaining to guess the number."
        )

        # asking user to guess a number
        users_guess = int(input("Make a Guess: "))

        # if guessed number is less than answer, give feedback and reduce number of attempts by 1.
        if users_guess < chosen_number:
            print("Too Low")
            attempts_remaining -= 1
        # if guess number is greater than answer, give feedback and reduce number of attempts by 1.
        elif users_guess > chosen_number:
            print("Too High")
            attempts_remaining -= 1
        # if guess is equal to answer, give feedback, and set game over equal to True
        elif users_guess == chosen_number:
            print(f"You Win! The number was {chosen_number}")
            game_over = True

        # if the user ran out of attempts and their last guess was also incorrect, then they lose
        # give feedback, reveal the answer, and set game over equal to True
        if attempts_remaining == 0 and users_guess != chosen_number:
            print(f"You ran out of attempts, You Lose! The number was {chosen_number}")
            game_over = True

# keep playing as long as the user wants, between every game clear the console.
playing = True
while playing:
    continue_playing = input(
        "Do you want to play the number guessing game? Type 'y' or 'n': ")
    if continue_playing == 'y':
        system('clear')
        guess_the_number()
    else:
        playing = False

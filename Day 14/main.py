from game_data import data
from art import logo, vs
from random import choice
from os import system


"""Get a random data from game_data, format it and return formatted string and score value."""
def get_a_card():
    # selecting random data from game_data
    random_choice = choice(data)
    # setting variables
    name = random_choice['name']
    description = random_choice['description']
    country = random_choice['country']
    card_score = random_choice['follower_count']
    # generating formatted string
    card = f"{name}, {description}, from {country}"
    # returning a list of formatted string and score
    return [card, card_score]


"""Compare the scores to get the right answer."""
def compare_scores(score_a, score_b):
    if score_a > score_b:
        return "A"
    else:
        return "B"


"""Compares user's guess with right answer."""
def check_answer(guess, answer):
    if guess == answer:
        return True
    else:
        return False


def higher_lower():
    # initializing
    choice_A = get_a_card()
    choice_B = get_a_card()
    score = 0
    should_continue_playing = True

    # while playing
    while should_continue_playing:
        # set choice A equal to choice B
        choice_A = choice_B
        # as long as choice B and choice A are equal, get a new choice
        while choice_B == choice_A:
            choice_B = get_a_card()

        # set card and score for choice A
        card_A = choice_A[0]
        score_A = choice_A[1]

        # set card and score for choice B
        card_B = choice_B[0]
        score_B = choice_B[1]

        # get the actual answer
        winning_card = compare_scores(score_A, score_B)

        # print the two cards
        print(f"Card A: {card_A}")
        print(vs)
        print(f"Card B: {card_B}")

        # ask the user to make a guess
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # if user's guess is equal to the right answer, add a point to score and continue the game
        if check_answer(user_guess, winning_card):
            system("clear")
            print(logo)
            score += 1
            print(print(f"You're right! Your current score: {score}"))
        else:
            # if user's guess is not equal to right answer, display the final score and stop the game.
            system("clear")
            print(logo)
            print(f"Sorry, that's wrong. Final Score: {score}")
            should_continue_playing = False


# print logo and start the game
print(logo)
higher_lower()
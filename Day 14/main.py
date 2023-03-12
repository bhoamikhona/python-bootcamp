from game_data import data
from art import logo, vs
from random import choice
from os import system

"""Get a random data from game_data, format it and return formatted string and score value."""
def get_a_card():
    random_choice = choice(data)
    name = random_choice['name']
    description = random_choice['description']
    country = random_choice['country']
    card = f"{name}, {description}, from {country}"
    card_score = random_choice['follower_count']
    return [card, card_score]

"""Compare the scores to get the right answer."""
def compare_scores(score_1, score_2):
    if score_1 > score_2:
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
    choice_A = get_a_card()
    choice_B = get_a_card()
    score = 0
    should_continue_playing = True

    while should_continue_playing:
        choice_A = choice_B
        while choice_B == choice_A:
            choice_B = get_a_card()

        card_A = choice_A[0]
        score_A = choice_A[1]

        card_B = choice_B[0]
        score_B = choice_B[1]

        winning_card = compare_scores(score_A, score_B)

        
        print(f"Card A: {card_A}")
        print(vs)
        print(f"Card B: {card_B}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if check_answer(user_guess, winning_card):
            system("clear")
            print(logo)
            score += 1
            print(print(f"You're right! Your current score: {score}"))
        else:
            system("clear")
            print(logo)
            print(f"Sorry, that's wrong. Final Score: {score}")
            should_continue_playing = False
        
print(logo)
higher_lower()
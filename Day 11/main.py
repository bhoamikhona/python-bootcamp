# imports
from art import logo
from random import choice
from os import system

# initialization
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_playing = True


'''Returns a random card from card deck.'''
def deal_a_card():
    return choice(card_deck)

'''Take a list of cards and return the sum calculated from the cards.'''
def calculate_score(hand):
    hand_total = sum(hand)
    # if there are 2 cards in the hand and they total to 21 i.e. 10 + 11, then it is blackjack, and in this case 0 represents blackjack
    if len(hand) == 2 and hand_total == 21:
        return 0

    # if the total of the hand is greater than 21 and there is an ace, then taking the value of ace = 1 instead of ace = 11
    if hand_total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

    # returning the total of the hand
    return sum(hand)


'''Compares user score and computer score and returns the result.'''
def compare_scores(user_score, computer_score):
    # if scores are equal, it is a draw
    if user_score == computer_score:
        return "Draw!"
    # if computer has a blackjack then user loses
    elif computer_score == 0:
        print("You Lose! Oponent has a Blackjack!")
    # if user has a blackjack then computer loses
    elif user_score == 0:
        print("You Win! You have a Blackjack!")
    # if user's hand value is greater than 21, user loses
    elif user_score > 21:
        return "You Lose! You went over 21!"
    # if computer's hand value is greater than 21, user wins
    elif computer_score > 21:
        return "You Win! Your Oponent went over 21!"
    # if computer's hand value is greater than user's hand value, user loses
    elif user_score < computer_score:
        return "You Lose! Your Oponent has higher score than you!"
    # if user's hand value is greater than computer's hand value, user wins
    elif user_score > computer_score:
        return "You win! You have higher score than your oponent!"

def blackjack():
    # printing logo
    print(logo)

    # initializing
    user_hand = []
    computer_hand = []
    game_not_over = True
    
    # dealing cards
    for _ in range(2):
        user_hand.append(deal_a_card())
        computer_hand.append(deal_a_card())

    while game_not_over:
        
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        
        # revealing user cards and the first card of computer to the user
        print(f"Your cards: {user_hand}, Your current score: {user_score}")
        print(f"Oponents's first card: {computer_hand[0]}")

        # if user's score is greater than 21 or user or computer have a blackjack, the game is over
        if user_score > 21 or user_score == 0 or computer_score == 0:
            game_not_over = False
        else:
            # asking user if they would like to draw another card
            draw_another_card = input("Do you want to draw another card? Type 'y' or 'n': ")
            # if yes, then another card is added to user's hand and the next time while loop runs, user's score will be re-evaluated
            if draw_another_card == 'y':
                user_hand.append(deal_a_card())
            # if no, game is over
            else:
                game_not_over = False

    # computer will keep drawing cards if as long as it does not have a blackjack and its score is below 17
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_a_card())
        computer_score = calculate_score(computer_hand)

    # revealing all cards and scores and declaring results
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Oponent's final hand: {computer_hand}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))
    
# asking user if they would like to play a game of blackjack
while continue_playing:
    keep_playing = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ")
    if keep_playing == 'n':
        continue_playing = False
    else:
        system('clear')
        blackjack()
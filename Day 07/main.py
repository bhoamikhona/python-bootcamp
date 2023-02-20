# imports
import os
from random import choice
from hangman_art import stages, logo
from hangman_words import word_list

# initializing
chosen_word = choice(word_list)
lives = 6
display = []
end_of_game = False

# logo
print(logo)

# For Testing Purpose
# print(f"Chosen Word: {chosen_word}")

# Creating Blanks
for _ in chosen_word:
    display.append("_")

while not end_of_game:
    # Asking user to guess a letter
    guess = input("Guess a letter: ").lower()

    # clearing console after every while loop iteration
    os.system('clear')

    # if the user has already guessed the letter, notifying them
    if guess in display:
        print(f"\nYou've already guessed {guess}")

    # checking if the user's guessed letter is in the word, if so, then replacing the blank with the guessed letter
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    # converting 'display' list into a string and then printing it. Each list item is separated by a space character
    print(f"\n{' '.join(display)}")

    # if the guessed letter is not in the word, notifying the user, and decreasing the number of lives left.
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        # if no lives left, ending the game i.e. stepping out of while loop, and notifying the user
        if lives == 0:
            end_of_game = True
            print("\nYou Lose!")

    # if all the blanks are replaced with letters i.e. user has guessed the word correctly without losing all lives, the user wins, and notifying them about it.
    if "_" not in display:
        end_of_game = True
        print("\nYou Win!")

    # print hangman lives stages ascii art based on how many lives left
    print(stages[lives])

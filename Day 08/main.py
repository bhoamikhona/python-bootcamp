# imports
from art import logo

# initializing
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# caesar cipher function
def caesar_chiper(start_text, shift_amount, cipher_direction):
    # for decrypting the code
    if cipher_direction == "decode":
        shift_amount *= -1

    end_text = ""
    for char in start_text:
        # checking if current letter is alphabet or no
        if char in alphabet:
            # fetching index of current letter
            position = alphabet.index(char)
            # adding shift amount to the fetched index
            position += shift_amount
            # appending the letter located at the new index
            end_text += alphabet[position]
        else:
            end_text += char
    # printing result
    print(f"The {cipher_direction}d message is: {end_text}")
    
print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # this is for shift amounts that are greater than 26
    shift = shift % 26
    
    caesar_chiper(text, shift, direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if result == "no":
        should_continue = False
        print("Goodbye!")
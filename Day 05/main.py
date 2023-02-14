import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

####################################################################

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""

# for letter in range(nr_letters):
#     random_index = random.randint(0, len(letters) - 1)
#     password += letters[random_index]

# for symbol in range(nr_symbols):
#     random_index = random.randint(0, len(symbols) - 1)
#     password += symbols[random_index]

# for number in range(nr_numbers):
#     random_index = random.randint(0, len(numbers) - 1)
#     password += numbers[random_index]

# print(f"Your password is: {password}")

####################################################################

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for i in range(nr_letters):
  random_letter = random.choice(letters)
  password_list.append(random_letter)

for i in range(nr_numbers):
  random_number = random.choice(numbers)
  password_list.append(random_number)

for i in range(nr_symbols):
  random_symbol = random.choice(symbols)
  password_list.append(random_symbol)

random.shuffle(password_list)

password = ""

for i in password_list:
    password += i

print(f"Your password is: {password}")
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#1. Greeting
print("Welcome to the Tip Calculator.")

#2. Total Bill
bill = float(input("What was the total bill? $"))

#3. Percent of Tip
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#4. Number of People
people = int(input("How many people to split the bill? "))

#5. Calculation
percent = 1.00 + tip / 100
individual_bill = (bill / people) * percent
formatted_individual_bill = "{:.2f}".format(individual_bill)

#6. Result
print(f"Each person should pay: ${formatted_individual_bill}")

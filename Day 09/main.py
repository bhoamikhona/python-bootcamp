# imports
from os import system
from art import logo

# printing logo
print(logo)

# initializing
bids = {}
more_bidders = True

# function to find highest bidder
def find_highest_bidder(bidding_record):
    # initializing higest bid to 0
    highest_bid = 0
    # looping through bid record, if the bid in the record is higher than highest_bid then setting its value to the bid.
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            highest_bidder = bidder
    # print the final result
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

while more_bidders:
    # bidder name
    bidder_name = input("What is your name? ")
    # bid price
    bid_price = int(input("What is your bid? $"))
    # storing the bidder name (value) and bidder price (key) in dictionary 
    bids[bidder_name] = bid_price

    # asking if there are more bidders
    another_bidder = input("Is there another bidder? 'yes' or 'no': ").lower()

    # If there are no more bidders, stop the while loop, call the find_highest_bidder function and reveal the winner
    if another_bidder == "no":
        more_bidders = False
        find_highest_bidder(bids)
    # If there are more bidders, clear the screen, so the next bidder cannot see previous bidder's bid, and run the while loop again.
    elif another_bidder == "yes":
        system('clear')

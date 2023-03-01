# Day 11 - Blackjack (Capstone Project)

**About:** Today's project is all about applying everything that I have learned up until day 10 in one big project, which is Blackjack.

![blackjack](https://user-images.githubusercontent.com/50435319/221824567-b42fa8f3-b0eb-45ed-8b68-fc0d53caaedf.png)

## How to Play

- Blackjack is a gmae that's played using conventional deck of 52 playing cards.
- The goal of the game is to add up your cards to the largest number without going over 21.
- If the cards in your hand add up to more than 21, then it's called a bust and it mean that you lose immediately, and it doesn't matter how much you've gone over 21, as long as it's over 21, then you lose.
- Now the way that the cards are counted is that all the cards from 2 to 10 count as their face value. So, a 6 is a six and a 9 is nine etc. but, the Jack, Queen, and King each count as 10 and the other special card is the Ace.
- Ace can either count as a one towards your total, or it can count as a 11. Depending on whether if you've gone over 21 or whether if you're under 21, you can decided which value you want your Ace to represent.
- Let's say that the dealer got a 10 begin with and you got a queen which also counts as a 10 to begin with. So, these are the first cards that are dealt and both of these cards are revealed. The dealer then deals another card to each of you. Now, the dealer's second hand is concealed so you can't work out what their total is but, you can see your own card which lets take in our example as 3.
- So, the moment we don't know what the dealer has, it might be 10 plus anything but, we know that our score is 13, 10 + 3.
- At this point, you might ask the dealer for another card which turns out to be 7. So, now you have three cards and luckily it adds up to 20 without going over 21 but, there is also a possibility that you might've gotten a card that would have pushed your total over 21 at which point you would have lost, and it won't matter what dealer had, if your hand value went over 21, you lose.
- But we were lucky to get a 7 which adds our hand value to 20. Now, at this point we say we don't want any more cards and the dealer reveals their hand. If in this case, you and dealer both have 20 then it is draw. If you have 20 and dealer has 18 (i.e. your hand value > dealer's hand value), you win, and if you had 20 and dealer had 21 (i.e. your hand value < dealer's hand value) you lose.

## Our Blackjack House Rules

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The the Ace can count as 11 or 1.
- Use the following list as the deck of cards:
- cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.

## Lessons Learned

- `list1.extend(list2)` - The `extend()` method adds the specified list elements (or any iterable) to the end of the current list.
- `list1 += list2` - Is a shorthand way for writing the python `list1.extend(list2)` function. Both ways will give the same result.
- `list.remove(item)` - The `remove()` method removes the first occurence of the element with the specified value.

## Demo

[Demo Link](https://replit.com/@bhoamikhona/blackjack?v=1)

![blackjack-gif](https://user-images.githubusercontent.com/50435319/221825930-c018a3c8-f476-4b44-9a70-9b7367cd5dca.gif)

## Authors

- [@bhoamikhona](https://github.com/bhoamikhona)

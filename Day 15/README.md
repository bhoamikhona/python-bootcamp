# Day 15: Coffee Machine

**About:** Today we're going to set up local development environment for Python and we're going to be building a Coffee Machine Project. So, according to when the course was designed, the instructor wanted us to get up and running as fast as possible and start coding straight away, hence the use of [replit.com](https://replit.com/~). But, as the projects get more and more complex, then it's really important to start thinking about setting up a proper development environment.

**Coffee Machine Project:** In this project, we're going to make a digital version of a Coffee Machine. This coffee machine will make 3 flavors viz 1. espresso 2. latte and 3. capuccino. Each of these recipes require different quantities of water, coffee, and milk; and they have a different price. In addition, the coffee machine has some resources that it has to manage. It starts outs with 300ml of water in the tank, 200ml of milk, and 100g of coffee. The second feature of the coffee machine is that it's coin operated. We will use American coins and they have 4 types of coins viz Penny (1 cent = $0.01), Nickel (5 cents = $0.05), Dime (10 cents = $0.10), and Quarter (25 cents = $0.25).

**Project Requirements:**
- Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
  - Check the user's input to decide what to do next.
  - The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
- Turn off the Coffee Machine by entering "off" to the prompt.
  - For maintainers of the coffee machine, they can use "off" as the secret word to turn off the machine. Your code should end execution when this happens.
- Print Report
  - When the user enters "report" to the prompt, a report should be generated that shows the current resource values e.g.
    - "Water: 100ml"
    - "Milk: 50ml"
    - "Coffee: 76g"
    - "Money: $2.5"
- Check resources sufficient?
  - When the user chooses a drink, the program should check if there are enough resources to make that drink.
  - e.g. If Latte requires to 200ml of Water but, there is only 100ml left in the machin, it should not continue to make the drink but, print "Sorry, there is not enough Water."
  - The same should happen if another resource is depleted, e.g. milk or coffee.
- Process Coins
  - If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
  - Remember that quarters = $0.25, dimes = $0.10, nickels = $0.05, pennies = $0.01
  - Calculate the monetary value of the coins inserted e.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + (0.10 * 2) + 0.05 + (0.01 * 2) = $0.52
- Check transaction successful?
  - Check that the user has inserted emough money to purchase the drink they selected. e.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say "Sorry that's not enough money. Money refunded.".
  - But if the user has inserted emough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time "report" is triggered e.g.:
    - "Water: 100ml"
    - "Milk: 50ml"
    - "Coffee: 76g"
    - "Money: $2.50"
  - If the user has inserted too much money, the machine should offer change. e.g. "Here is $2.45 dollars in change." The change should be rounded to 2 decimal places.
- Make Coffee
  - If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
  - e.g. Report before purchasing latte:
    - "Water: 300ml"
    - "Milk: 200ml"
    - "Coffee: 100g"
    - "Money: $0"
  - e.g. Report after purchasing latte:
    - "Water: 100ml"
    - "Milk: 50ml"
    - "Coffee: 76g"
    - "Money: $2.50"
  - Once all resources have be deducted, tell the user "Here is your latte. Enjoy!". If latte was their choice of drink.

![coffee-machine]()

## Lessons Learned

- Setup Local Development Environment
- Installing Python Locally
- IDE: Integrated Development Environment
  - This is a piece of software that helps you as you're creating your code by linting your code, finding errors, giving guidance on coding style, debugging, and just making life easy as you're writing more and more code.
- In this course, we're going to use [PyCharm](https://www.jetbrains.com/pycharm/)
- Python Style Guide: PEP 8

## Demo

[Demo Link]()

![demo-gif]()

## Authors

- [@bhoamikhona](https://github.com/bhoamikhona)

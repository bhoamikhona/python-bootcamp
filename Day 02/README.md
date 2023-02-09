# Day 02 - Tip Calculator

**About:** A tip calculator that asks you total bill, number of people to split the bill between, and percentage of tip to add. It does the calculation for you, taking into account all the information that you provide and tells you how much should each person pay.

![tip calculator](https://user-images.githubusercontent.com/50435319/181641546-89de2080-5388-466b-9002-388f24c14a93.png)

## Lessons Learned

- Data Types
  - String
  - Integer
  - Float
  - Boolean
- Subscripting or Subscript: A method of pulling out a particular element from a string.
  - `print("Hello"[0])` This will pull out the first character i.e. "H" from the string "Hello".
  - NOTE: The indexes start from 0, not from 1.
- Errors:
  - Type Error
- Type Checking
  - Type Function: `type(23)` -> `<class 'int'>`
- Type Conversion
  - Convert to int: `int(12.67)` -> 12
  - Convert to float: `float(15)` -> 15.0
  - Convert to string: `str(24)` -> "24"
- Mathematical Operations
  - add: +
  - subtract: -
  - multiply: \*
  - divide: /
  - exponent: \*\*
  - floor division: //
  - PEMDAS-LR (parentheses, exponents, multiply and division, add and subtract) from Left to Right
- NOTE: Whenever we use division, the result is always going to be a float, even if the dividend and divisor are int or any other data type, the result will always be float.
- NOTE: When we use floor division, the result will always be int as it will round to nearest lower integer of the floating point number.
- Mathematical Shorthand
  - `+=`, `-=`, `*=`, `/=`
- Rounding Numbers
  - Round Function: `round(3.14159265359, 2)` -> 3.14
- f-String
- Formatting
  - Format Function: `string.format(value1, value2...)`
  - To understand better look at the first response on this [query](https://stackoverflow.com/questions/58171983/need-help-understanding-the-format-2f-command-and-why-it-is-not-working-in-my).

## Demo

[Demo Link](https://replit.com/@bhoamikhona/tip-calculator?v=1)

![tip-calculator-gif](https://user-images.githubusercontent.com/50435319/217828275-089fd735-6d95-4362-b26f-c2b86048b617.gif)

## Authors

- [@bhoamikhona](https://github.com/bhoamikhona)

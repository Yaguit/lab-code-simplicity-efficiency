"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

a = int(input('Welcome to this calculator! \nIt can add and subtract whole numbers from zero to five \nChoose one number (0 to 5): '))
b = input('One operator (+ or -): ')
c = int(input('And another number (0 to 5): '))

if b == '+':
    print(f'{a} plus {c} equals {a+c} \nThanks for using this calculator, goodbye :)')
if b == '-':
    print(f'{a} minus {c} equals {a-c} \nThanks for using this calculator, goodbye :)')
if (a < 0) or (a > 5) or (c < 0) or (c > 5) or (b != '+' and b != '-'):
    print("I am not able to answer, check your input.")
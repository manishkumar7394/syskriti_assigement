# TaskPY200_T2
'''This assignment is based on conditional statements in Python.
The objective of this program is to check whether a number entered by the user is positive, negative, or zero.
The program also displays the positive value if the number is negative using formatted string printing.'''

# Program to check if a number is positive, negative, or zero

number = float(input("Enter a number: "))

if number > 0:
    print(f"Your entered number {number} was positive.")

elif number < 0:
    print(f"Your entered number {number} was negative, however positive value of your number is {abs(number)}.")

else:
    print(f"Your entered number {number} was zero.")


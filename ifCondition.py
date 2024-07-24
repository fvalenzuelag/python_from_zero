# Author: Francisca Valenzuela Garrido

# This file contains the condition "if" and its variations.

# The structue of an if statement is:
# if condition:
#     code // This code will only run if the condition is True
# The code inside the if statement must be indented.

answer = int(input("Enter your age: ")) # Remember to cast the input to the desired data type

if answer < 18:
    print("You are a minor.")

# Adding the else statement
if answer < 18:
    print("You are a minor.")
else:
    print("You are an adult.") # This code will only run if the condition is False

# Adding the elif statement

if answer < 18:
    print("You are a minor.")
elif answer < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Nested if statements

tempAnswer = int(input("Enter the current temperature in Celsius: "))

if tempAnswer < 0:
    print("It is freezing.")
    if tempAnswer < -10:
        print("Stay at home.")
    else:
        print("Wear a coat.")
elif tempAnswer < 10:
    print("It is cold.")
    if tempAnswer < 5:
        print("Wear a coat.")
    else:
        print("Wear a jacket.")
elif tempAnswer < 20:
    print("It is warm.")
    if tempAnswer < 15:
        print("Wear a jacket.")
    else:
        print("Wear a sweater.")
else:
    print("It is hot.")
    if tempAnswer < 30:
        print("Wear a sweater.")
    else:
        print("Wear a t-shirt.")

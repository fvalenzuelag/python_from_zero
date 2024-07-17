# Author: Francisca Valenzuela Garrido

# This file contains the definition of common variables in Python and it's declaration

# A variable can't start with a number or special character except for underscore (_)

# Snake Case
my_variable = 'Hello, World!'

# Camel Case
myVariable = 'Hello, World!'

# Pascal Case
MyVariable = 'Hello, World!'

# Constants
PI = 3.14159

# Example of a calculation with variables and input
# input() function is used to get input from the user and it always returns a string

# Get the radius from the user
radius = float(input('Enter the radius of the circle: '))
# Calculate the area of the circle
area = PI * radius ** 2

# Print the area of the circle
print(f'The area of the circle with radius {radius} is {area}')
# The output will be: The area of the circle with radius 5.0 is 78.53975
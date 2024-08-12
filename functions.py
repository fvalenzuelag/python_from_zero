# Author: Francisca Valenzuela Garrido

# This file contains methods and functions. 

# def is a keyword that is used to define a function. The function name is followed by parentheses and a colon. The code inside the function must be indented.
# def is a protected word in Python, so it cannot be used as a variable name.

# The function is defined with the def keyword, followed by the function name and parentheses. The parentheses can contain parameters that the function will receive. The code inside the function must be indented.
# Functions will only run if they are called.
# Return is also a protected word in Python, so it cannot be used as a variable name.

# The mod operator (%) returns the remainder of the division of two numbers. 
# If the remainder is not 0, the number is odd.

def is_even(value):
    number = int(value) # Remember to cast the input to the desired data type
    if(number%2)== 0:
        return print("The number is even.")
    else:
        return print("The number is odd.")
# Be careful with the indentation. The code inside the function must be indented.

# Test out the function:
is_even(5)
is_even(6)

def is_valid_mail(text_input):
    email = str(text_input)
    if(email.find("@") != -1) and email.find(".") != -1: 
    # The find() method returns the index of the first occurrence of the specified value.
        return print("The email is valid.")
    else:
        return print("The email is not valid.")
    
# Test out the function:
is_valid_mail("mike@yahoo")
is_valid_mail("mike.yahoo.com")
is_valid_mail("mike@yahoo.com")

def average_number():
    # The input() function returns a string, so it must be cast to the desired data type.
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    number4 = int(input("Enter the fourth number: "))
    number5 = int(input("Enter the fifth number: "))
    average = (number1 + number2 + number3 + number4 + number5) / 5
    return print("The average is: ", average)

# Test out the function:
average_number()

# Save the function return value in a variable
def calendar():
    day = input("Enter the day: ")
    month = input("Enter the month: ")
    year = input("Enter the year: ")
    return day, month, year

# Test out the function:
day, month, year = calendar()
print("The date is: ", day + '/' + month + '/' + year)
# The output will look like this: The date is:  10/10/2021
# The order of the variables must match the order of the return values.
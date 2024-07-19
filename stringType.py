# Author: Francisca Valenzuela Garrido

# This file contains the explanation of the string data type in Python
# A String starts in index 0, the word 'Hello' starts in index 0 and ends in index 4

# A string is a sequence of characters enclosed in single, double, or triple quotes

# Main Function in Python to know the methods available
print(dir()) # This will return a list of the attributes and methods of Python
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# String Methods
print(dir(str)) # This will return a list of the attributes and methods of the string data type

# Concatenation
firstString = 'Hello, '
secondString = 'World!'
print(firstString + secondString) # This will return: Hello, World!

# Formatting
# Capitalize the first letter of the string
message = 'hello, world!'
print(message.capitalize()) # This will return: Hello, world!

# Convert the string to uppercase
print(message.upper()) # This will return: HELLO, WORLD!

# Convert the string to lowercase
print(message.lower()) # This will return: hello, world!

# Replace a substring in the string
print(message.replace('world', 'Python')) # This will return: hello, Python!

# Swap the case of the string
print(message.swapcase()) # This will return: HELLO, WORLD!
message = 'HELLO, WORLD!'
print(message.swapcase()) # This will return: hello, world!

# Center the string
message = 'Hello, World!'
print(message.center(20)) # This will return:   Hello, World!
print(message.center(20, '*')) # This will return: ***Hello, World!***

# Justify the string
print(message.ljust(20)) # This will return: Hello, World! (Left Justify)
print(message.rjust(20)) # This will return: Hello, World! (Right Justify)

# Searching at the string
message = 'This is a beautiful day!'
print(message.count('a')) # This will return: 3
print(message.find('a')) # This will return: 8, 8 is the index of the first 'a' in the string
print(message.rfind('a')) # This will return: 19, 19 is the index of the last 'a' in the string
print(message.find('Python')) # This will return: -1, -1 means that the substring is not found in the string
print(message.find('a',0,10)) # This will return: 8, 8 is the index of the first 'a' in the string from index 0 to 10

# Validate the string
message = 'Hello, World!'
print(message.isdigit()) # This will return: False (The string is not a digit)
print(message.isalpha()) # This will return: False (The string is not an alphabet)
print(message.isalnum()) # This will return: False (The string is not an alphanumeric)
print(message.isspace()) # This will return: False (The string is not a space)
print(message.islower()) # This will return: False (The string is not lowercase)
print(message.isupper()) # This will return: False (The string is not uppercase)
print(message.istitle()) # This will return: True (The string is a title)

# Size of the string
message = 'Hello, World!'
print(len(message)) # This will return: 13
print(message.__len__()) # This will return: 13
# Both methods are the same, but the first one is the recommended one
# Author: Francisca Valenzuela Garrido

# This file contains the definition of the class DataType, which is used to represent the data type of a variable in Python
# In Python there are several data types, such as int, float, str, bool, list, tuple, dict, etc.

# To see which type of data type a variable has, we can use the function type() in Python

# Int
x = 5
print(type(x)) # <class 'int'>

# Float
y = 5.0
print(type(y)) # <class 'float'>

# String
msg = "Hello, World!" # or 'Hello, World!' or """Hello, World!""" or '''Hello, World!'''
print(type(msg)) # <class 'str'>

# Bool
flag = True # or False
print(type(flag)) # <class 'bool'>

# List
numericList = [1, 2, 3, 4, 5] # list can be modified
print(type(numericList)) # <class 'list'>

# Tuple
numericTuple = (1, 2, 3, 4, 5) # tuple can not be modified
print(type(numericTuple)) # <class 'tuple'>

# Dict
person = {"name": "John", "age": 36}
print(type(person)) # <class 'dict'>

# None
nothing = None
print(type(nothing)) # <class 'NoneType'>

# Type casting is the way to convert a variable from one data type to another data type
# For example, to convert a float to an int, we can use the function int()
x = 5.74
y = int(x)
print(y) # 5 - the decimal part will be truncated, not rounded

# To convert an int to a float, we can use the function float()
x = 9
y = float(x)
print(y) # 9.0

# To convert a number to a string, we can use the function str()
x = 70
numberAsString = str(x)
print(numberAsString) # '70' - We can not apply the same for a list, tuple or dict

# Boolean as a special case, when the number is different to 0, the result is True, otherwise False
x = 0
y = bool(x)
print(y) # False
x = -1034
y = bool(x)
print(y) # True
x = 593
y = bool(x)
print(y) # True

# Author: Francisca Valenzuela Garrido

# This file contains the loop methods and their variations.

# In order to print a list of X elements and not use the "print" function X times, we can use a loop.
# The most common loops are "for" and "while".

# For
# The structure of a for loop is:
# for variable in iterable:
#     code // This code will run for each element in the iterable
# The code inside the for loop must be indented.

listNames = ['Alice','Bob','Charlie','David','Eve']

for name in listNames:
    print(name)

# This can also be made for a tuple

tupleNumbers = (1,2,3,4,5)

for number in tupleNumbers:
    print(number)

# And for a set

setLetters = {'a','b','c','d','e'}

for letter in setLetters:
    print(letter)

# And for a dictionary
# The loop will iterate over the keys of the dictionary

dictNames = {1:'Alice',2:'Bob',3:'Charlie',4:'David',5:'Eve'}

for key in dictNames:
    print(key)

# We can also run the for loop for a desired size
# The range function will generate a sequence of numbers from 0 to n-1
# The structure of the range function is: range(start,stop,step)
# The start and step parameters are optional

for i in range(5):
    print(i)

# While

# The structure of a while loop is:
# while condition:
#     code // This code will run while the condition is True
# The code inside the while loop must be indented.
# There must be a way to break the loop, otherwise it will run forever.

counter = 0

while counter < 5:
    print(counter)
    counter += 1 # When it reaches 5, the condition will be False and the loop will stop

# We can also use the break statement to stop the loop

counter = 0

while True:
    print(counter)
    counter += 1
    if counter == 5:
        break

# The continue statement will skip the rest of the code inside the loop and go to the next iteration

# If we don't know the lenght of the iterable, we can use the len function
# The len function will return the number of elements in the iterable

listNames = ['Alice','Bob','Charlie','David','Eve']

while(counter < len(listNames)):
    print(listNames[counter]) # This will print the element at the current index
    counter+= 1 # This will increment the counter by 1

while(counter < listNames.__len__()):
    print(listNames[counter]) # This will print the element at the current index
    counter = counter + 1 # This will increment the counter by 1

# Additional methods for loops
# The enumerate function will return the index and the element of the iterable

for index, name in enumerate(listNames): # index will start at 0
    print(f'Index: {index}, Name: {name}')

# The zip function will return the elements of two or more iterables

listNumbers = [1,2,3,4,5]

for number, name in zip(listNumbers,listNames):
    print(f'Number: {number}, Name: {name}')

# Author: Francisca Valenzuela Garrido

# This file contains the set type and its methods.
# Set must have unique values, it does not allow duplicates.
# If duplicates are added, the set will only keep one of them.

setA = {'Hi',2,False,3.5} # Set with different data types
setB = {1,2,3,4,5,6,7,8,9,10} # Set with integers

# Check methods available for set
print(dir(setA)) # print(dir(set)) is also valid

# Accessing the set
print(setA)

# Building a set
newSet = set([1,2,3,4,5])
print(newSet)

# Adding a new value
setA.add('Hello')
print(setA)

# Removing a value
setA.remove(False)
print(setA)

# Copying a set
setACopy = setA.copy()
print(setACopy)

# Check for values in a set
existsIn = 2 in setA
print(existsIn) # True

# Check for subset in a set
# A subset is a set that contains all the elements of another set
subset = newSet.issubset(setB)
print(subset) # True

# Intersection, Union, Difference and Symmetric are the same as in mathematics

# Intersection of two sets
intersection = setA.intersection(setB)
print(intersection)
# This is the same than using the & operator
intersection = setA & setB
print(intersection)

# Union of two sets
union = setA.union(setB)
print(union)
# This is the same than using the | operator
union = setA | setB
print(union)

# Difference of two sets
difference = setA.difference(setB)
print(difference)
# This is the same than using the - operator
difference = setA - setB
print(difference)

# Symmetric difference of two sets
symmetricDifference = setA.symmetric_difference(setB)
print(symmetricDifference)
# This is the same than using the ^ operator
symmetricDifference = setA ^ setB
print(symmetricDifference)

# Clearing a set
setA.clear()
print(setA) # set()
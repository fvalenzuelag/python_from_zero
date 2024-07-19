# Author: Francisca Valenzuela Garrido

# This file contains the explanation of the list and tuple data types in Python
# A list is a sequence of elements enclosed in square brackets []
# A tuple is a sequence of elements enclosed in parentheses ()

# Obtaining the methods available for a list
print(dir(list)) # This will return a list of the attributes and methods of the list data type

# Obtaining the methods available for a tuple
print(dir(tuple)) # This will return a list of the attributes and methods of the tuple data type

# List
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 20, 'b', 30, 'c']
# List can have multiple data types

# Tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 20, 'b', 30, 'c')
# Tuple can have multiple data types

# Methods available for a list

# Concatenation
print(list1 + list2) # This will return: [1, 2, 3, 4, 5, 'a', 20, 'b', 30, 'c']

# Duplicate or triplicate the list
print(list1 * 2) # This will return: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(list2 * 3) # This will return: ['a', 20, 'b', 30, 'c', 'a', 20, 'b', 30, 'c', 'a', 20, 'b', 30, 'c']

# Append an element to the list
list1.append(6)
print(list1) # This will return: [1, 2, 3, 4, 5, 6]

# Extend the list with another list
list1.extend([7, 8, 9])
print(list1) # This will return: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Insert an element in the list
list1.insert(4, 10) # This will insert the element 10 in the index 4 and move the rest of the elements to the right
print(list1) # This will return: [1, 2, 3, 4, 10, 5, 6, 7, 8, 9]

# Remove an element from the list
list1.remove(10) # This will remove the element 10 from the list
print(list1) # This will return: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Remove the last element from the list
list1.pop() # This will remove the last element from the list
print(list1) # This will return: [1, 2, 3, 4, 5, 6, 7, 8]
list1.pop(3) # This will remove the element in the index 3 from the list
print(list1) # This will return: [1, 2, 3, 5, 6, 7, 8]

# Reverse the list
list1.reverse()
print(list1) # This will return: [8, 7, 6, 5, 3, 2, 1]

# Sort the list
list1.sort() # This will sort the list in ascending order but only if the list has the same data type
print(list1) # This will return: [1, 2, 3, 5, 6, 7, 8]
list2.sort(reverse=True) # This will sort the list in descending order but only if the list has the same data type
print(list2) # This will return: ['c', 'b', 'a', 30, 20]

# Search an element in the list
print(list1.index(5)) # This will return: 3, 3 is the index of the element 5 in the list

# Count the number of times an element appears in the list
print(list1.count(5)) # This will return: 1, 5 appears only once in the list

# Search max and min in the list
print(max(list1)) # This will return: 8, 8 is the maximum number in the list
print(min(list1)) # This will return: 1, 1 is the minimum number in the list

# Nested List
# A list can contain another list and that is called a nested list
nestedList = [1, 'Blue', 3, ['Red', 5, 6]]
# To print all the elements of the nested list
print(nestedList) # This will return: [1, 'Blue', 3, ['Red', 5, 6]]
# To print the first element of the nested list
print(nestedList[0]) # This will return: 1
# To print the second element of the nested list
print(nestedList[3][1]) # This will return: 5

# Change a tuple to a list
print(list(tuple1)) # This will return: [1, 2, 3, 4, 5]
# Change a list to a tuple
print(tuple(list1)) # This will return: (1, 2, 3, 5, 6, 7, 8)

# With the tuple convert into a list, you can use the methods of the list and change values
# Author: Francisca Valenzuela Garrido

# This file contains the dictionary type and its methods.

userData = {
    "name": "John",
    "age": 30,
    "Sex": "Masculine",
    "Country": ["Canada", "USA"],
}

# Check methods available for dictionary
print(dir(userData)) # print(dir(dict)) is also valid

# Accessing the dictionary
print(userData)
print(userData["name"]) # Print the value of the key "name"
print(userData["Country"]) # Print the values "Canada" and "USA"
print(userData["Country"][0]) # Print the value "Canada", [0] represent the first index

# Building a dictionary
newUserData = dict(name="John", age=45)
print(newUserData)

# Adding a new key-value pair
userData["City"] = "New York"
print(userData)

# Deleting a key-value pair
del userData["City"]
print(userData)

# Updating a key-value pair
userData["name"] = "Jane"
print(userData)

# Getting the keys
print(userData.keys())

# Getting the values of the keys
print(userData.values())

# Getting the key-value pairs
print(userData.items())

# Updating the dictionary
userData.update({"name": "John", "age": 30})
print(userData)

# Copying a dictionary
userDataCopy = userData.copy()
print(userDataCopy)

# Getting the value of a key
print(userData.get("name")) # Print the value of the key "name"

# Pop a key-value pair, delete the key-value pair and return the value
print(userData.pop("name"))

# Pop an item, delete the last key-value pair and return the key-value pair
print(userData.popitem())

# Clear the dictionary
userData.clear()
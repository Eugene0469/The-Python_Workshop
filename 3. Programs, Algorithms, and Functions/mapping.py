"""
Mapping with Lambda Fnctions
map function applies a given function to all items in a list.
It returns a generator object.
"""
'''
The goal is to count all the characters in the entire list and divide that value
with the number of elements so as to get the average number of characters per element.
'''
# Initialize a list
names = ["Eugene", "Abby", "Nyima", "Xavier"]

# Declare a list to store the lengths of each element in the list
length = []

'''
Method 1: Get the average number of characters in a list without using mapping
'''

# Use a for loop to find the length of each element in the list and store it in the list variable length

for name in names:
    # Use the append list function to add elements to the length list
    length.append(len(name))

# Calculate the average number of characters per element
print("Average number of characters per element(without using mapping):", sum(length) / len(length))

'''
Method 1: Get the average number of characters in a list using mapping
'''
# Use the map function to apply the len function to all the elements of the names list
length = list(map(len, names))

# Calculate the average number of characters per element
print("Average number of characters per element(using mapping):", sum(length) / len(length))



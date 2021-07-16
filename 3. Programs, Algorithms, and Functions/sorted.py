"""
Sorting with Lambda Functions
sorted function takes an iterable such as a list nd sorts them according to a function
"""
'''
The goal is to arrange the elements of a list according to the length of the elements
'''
# Initialize a list
names = ['Ming', 'Jennifer', 'Andrew', 'Boris']

# Use the sorted fucntion to sort the list according to the length
result = list(sorted(names, key = lambda name:len(name)))

'''
The above statement can be simplified by just passing in the len function rather than using a lambda:
result = list(sorted(names, key = len))
'''

# Print out the result
print(result)
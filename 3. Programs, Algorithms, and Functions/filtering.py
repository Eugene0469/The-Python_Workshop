"""
Filtering with Lambda Functions
filter function takes a function and iterables(e.g. list) as inputs and returns the elements
for which the fucntion returns True
"""
'''
The goal is to return the number of elements that are three letters long in a list variable names
'''
# Initialize a list variable
names = ['Karen', 'Jim', 'Kim']

# Use the filter function to return only elements that are three letter long
result = list(filter(lambda name: len(name) == 3, names))

# Print the results
print(result)

'''
The goal is to calculate the sum of all the multiples of 3 or 7 below 1,000
'''
# initialize a list to store all the natural numbers below 1000(0-999)
nums = list(range(1000))

# Use the filter function to find the multiples of 3 and 7 in the nums list
result = list(filter(lambda num: num%3 == 0 or num%7 == 0, nums))

# Print the total sum of these numbers
print(sum(result))
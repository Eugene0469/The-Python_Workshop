"""
The program applies the logistic function to a list of values
logistic function: f(x) = 1 / (1 + e**-x)
"""
import math

#  Initialize the list of values
nums = [-3,-5, 1, 4]

# Use the map function to pass the list of values in nums as argument x to a lambda function
result = list(map(lambda x: 1 / (1 + math.exp(-x)), nums))

# Print out the result
print(result)
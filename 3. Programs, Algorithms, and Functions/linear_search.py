"""
Linear Search in Python

This is a searching algorithm script that, if present, returns the position of a value in a list. 
It is a simple but inefficient agorithm with a time complexity of O(n)
"""
# Initialize a list
l = [4,6,1,8,2,7,0]

# Specify a value to search for
search_for = int(input("Enter the value you wish to search for: "))

# Create a result variable that has a default value of -1(indicating that the value being searched for is not in the list
result = -1

# Create a loop that searches for the value
for i in range(len(l)):
    if search_for == l[i]:
        result = i
        break

# Print out the result
print("Position of value in the list(if -1, the value is not in the list):", result)
"""
The script below finds the maximum from a list of positive numbers
"""
# initialize a list
l = [4,2,7,3]
# Set maximum variable to 0
maximum = 0

# Search for the maximum number in the list
for number in l:
    if number > maximum:
        maximum = number
# print out the maximum number
print("Maximum number:", maximum)
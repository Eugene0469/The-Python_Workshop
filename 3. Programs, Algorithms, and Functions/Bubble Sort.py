"""
Time Complexity of an Algorithm
This is the rship btwn the size of the problem and the steps taken

The script below is used to describe the Bubble Sort Algorithm that 
has a time complexity of O(n^2)
"""
# Initialize a list of numbers
l = [5,3,6,9,2,8,1]

# Print the unsorted list
print("Unsorted list:", l)

# Create an indicator that will tell us when you can stop looping through the array
still_swapping = True

# Look through each number, and compare it to maximum
while still_swapping:
    still_swapping = False
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            still_swapping = True

# Print the sorted list
print("Sorted list:", l)
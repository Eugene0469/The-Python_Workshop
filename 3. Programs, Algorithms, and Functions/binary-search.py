"""
The Binary Search Algorithm
It takes a SORTED array and finds the position of the target value.
"""
# Initialize an unsorted list
l = [4,1,2,7,3,6,9,0]

# Print out unsorted list
print("Unsorted list:",l)

# Use the bubble sort algorithm to sort the list
isSorted = True
while isSorted:
    isSorted = False
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            isSorted = True

# Print out sorted list
print("Sorted list:",l)

# Request user to search for the index of any item in the list
searchFor = int(input("Enter number from list to search for its index: "))

# Use the binary search algorithm to search for the number
sliceStart = 0
sliceEnd = len(l) - 1
isFound = False

while sliceStart <= sliceEnd and not isFound:
    location = (sliceStart + sliceEnd) // 2
    if l[location] == searchFor:
        isFound = True
    else:
        if l[location] < searchFor:
            sliceStart = location + 1
        else: 
            sliceEnd = location -1
            
# Print out the index of the number
print("Index of {} is: {}".format(searchFor, location))
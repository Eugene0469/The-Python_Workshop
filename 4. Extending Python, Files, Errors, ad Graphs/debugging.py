"""
Debugging methods include interactive debugging, unit testing,
integration testing, and other types of monitoring and rofiling practices.

Defensive programming ensures the continuing fucntion of a piece of program under
unforeseen circumstances.

Writing Assertions
Python provides the assert statement that assumes that the condition is always true 
and halts the program and raises an AssertionError message if it is false
eg:
    x = 2
    assert x < 1,"Invalid value"
    the program will run as long as x < 1 and will halt if otherwise, raising the
    assertion error message 'Invalid value'. 
You can also write the assert function without the optional error message
Asserts can be disabled globally and should not be used to check whether a function 
argument contains an invalid/unexpected value. They are debugging tools and are not to
be used to handle runtime errors.
"""
"""
The program calculates the average marks of a student and ensures that the user 
enters the correct parameters, raising an error message if otherwise
"""
'''
@brief: Calculates the average from a given list
@param: marks: list of marks
@retval: average mark rounded to 2 decimal places
'''
def avg(marks):
    assert len(marks) != 0, "Length of the marks list cannot be 0"
    return round(sum(marks)/len(marks), 2)

list1 = [73,82,62]
print("Average marks for list1[73,82,62]", avg(list1))
list2 = []
print("Average marks for list2[]", avg(list2))

"""
The if __name__ == "__main__" Statement

It is used when you want to be able to execute the script by itself, 
but also be able to import objects from the script as though it were 
a regular module.

When executing from the cmd line, the Python interpreter sets the special
__name__ variable equal to the '__main__' string, such that when you get 
to the end of the script, the result is printed. 
However, when importing result_2, the print statement is never reached
"""
# if you try importing result_1 in a Python console, it will print
# the result again
result_1, result_2 = 0, 0
for n in range(1,11): # This loops through 1 to 10, not including 11
    result_1 +=n
    result_2 +=n
print(result_1)
# To only call the print function in the case where __name__ == "__main__":
if __name__ == '__main__':
    print(result_2)

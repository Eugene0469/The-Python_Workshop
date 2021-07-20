"""
The program below reads contexts from a text file stored in the same directory
"""
'''
Initialize an object to store the contens of the file.
The open function takes the path of the text file as an argument and
returns an object
'''
f = open('pg37431.txt')
# Read the contents of the file and store it in a string variable text
text = f.read()
# Print out the contents of the file
# print(text)

print("*"*20,"Reading a part of a file","*"*20)
'''
We shall use the with statement to automatically close the preceding file object, f,
after the code block exits.
'''
with open('pg37431.txt') as f:
    print(f.read(5))
    
print("\n"+"*"*20,"Reading a text file line by line","*"*20)
with open('pg37431.txt') as f:
    print(f.readline())

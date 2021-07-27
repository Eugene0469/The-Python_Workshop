"""
The program displays student data as a bar graph
"""
import matplotlib.pyplot as plt
# Initialize a dictionary to store the grade and the corresponding number of students with that grade
studentData = {'A':20, 'B':30, 'C':10, 'D':5, 'E':8, 'F':2}

# add a title, x-axis label and y-axis label
plt.title('Grades Bar Plot for Biology Class')
plt.xlabel('Grade')
plt.ylabel('Num Students')

# Plot the bar chart with our dataset and customize the color command
plt.bar(list(studentData.keys()), list(studentData.values()), color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])

# Display the graph
plt.show()

# Plot the horizontal bar chart with our dataset and customize the color command
plt.barh(list(studentData.keys()), list(studentData.values()), color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])

# Display the graph
plt.show()
"""
The program plots a pie chart on the number of votes for each of the three candidates in an election for club president
"""
import matplotlib.pyplot as plt

# Initialize a dictionary to store the data(values do not need to be %ages
pollResult = {'Monica':230, 'Adrian':100, 'Jared':98}

# Add title to the chart
plt.title('Voting Result: Club President', fontdict = {'fontsize':20})

# Plot the pie chart
plt.pie(list(pollResult.values()), labels=list(pollResult.keys()), autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])

# Display the graph
plt.show()
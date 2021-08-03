"""
The program plots the results of an election both as a pie chart, sgowing the percentage 
and as a bar graph, showing the actual votes in one chart, using subplots in matplotlib
"""
import matplotlib.pyplot as plt

# Split the figure into two plots
fig = plt.figure(figsize = (8,4))
ax1 = fig.add_subplot(121) # 121 means split into 1 row, 2 columns and put in 1st part
ax2 = fig.add_subplot(122) # 122 means split into 1 row, 2 columns and put in 2nd part

# Initialize your dataset
labels = ['Adrian', 'Monica', 'Jared']
num = [230, 100, 98]

# Plot the pie chart to show the percentages
ax1.pie(num, labels = labels,  autopct = '%1.1f%%', colors = ['lightblue', 'lightgreen', 'yellow'])
ax1.set_title('Pie Chart (Subplot 1)')
        
# Plot the Bar Chart
ax2.bar(labels, num, color = ['lightblue', 'lightgreen', 'yellow'])
ax2.set_title('Bar Chart (Subplot 2)')
ax2.set_xlabel('Candidate')
ax2.set_ylabel('Votes')
fig.suptitle('Voting Results', size = 14)

plt.show()
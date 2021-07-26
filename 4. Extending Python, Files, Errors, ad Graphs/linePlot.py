"""
The program plots a line chart showing the growth of stock price
against the number of days
"""
import matplotlib.pyplot as plt

# Initialize our stock price data list
stock_price = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42, 200.32, 200.32, 200.85, 199.2, 199.2, 199.2, 199.46, 201.46, 197.54, 201.12, 203.12, 203.12, 203.12, 202.83, 202.83, 203.36, 206.83, 204.9, 204.9, 204.9, 204.4, 204.06]

# Initialize the number of days list(in our case, for the month of March)
t = list(range(1,31))
# Plot the graph
plt.plot(t, stock_price, marker='.', color='red')
# Define the numbers on the x-axis
plt.xticks([1,8,15,22,28])
# Set the title, x-axis label and y-axis label of the graph
plt.title('Opening Stock Prices')
plt.xlabel('Days')
plt.ylabel('$ USD')
# Display the graph
plt.show()
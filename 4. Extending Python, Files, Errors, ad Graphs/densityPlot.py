"""
Using the seaborn library, we plot a density graph.
Seaborn is a data visualization library based on matplotlib and provides visual graphs and support charts that are not available in matplotlib.
"""
import seaborn as sns
# Initialize ur data set
data = [90, 80, 50, 42, 89, 78, 34, 70, 67, 73, 74, 80, 60, 90, 90]
# Plot our density chart
sns.distplot(data)

# Configure the title and axes labels
import matplotlib.pyplot as plt
plt.title('Density Plot')
plt.xlabel('Score')
plt.ylabel('Density')

# Display the plot
plt.show()
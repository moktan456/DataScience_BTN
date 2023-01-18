# Activity 1 - Task 1
import matplotlib.pyplot as plt

# Create some data for the line graph
years = [2015, 2016, 2017, 2018, 2019, 2020]
rainfall = [2000, 2500, 3000, 3500, 4000, 4500]

# Plot the data as a line graph
plt.plot(years, rainfall)

# Add labels and a title to the graph
plt.xlabel('Years')
plt.ylabel('Rainfall (mm)')
plt.title('Rainfall in Bhutan over the years')

# Show the graph
plt.show()




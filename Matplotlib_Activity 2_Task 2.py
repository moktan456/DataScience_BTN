# Activity 2 - Task 2
import matplotlib.pyplot as plt

academic_year = [2016, 2017, 2018, 2019, 2020, 2021]
pass_percentage = [85.69, 91.45, 86.77, 91.55, 90.63, 82]

# Plot the data as a scatter plot
plt.bar(academic_year, pass_percentage)

# Add labels and a title to the plot
plt.xlabel('Academic Year')
plt.ylabel('Pass Percentage')
plt.title('BCSE Pass Percentages for Past 6 Years')

# Show the plot
plt.show()







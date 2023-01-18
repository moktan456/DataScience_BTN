# Activity 2 - Task 1
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

# Data showing the number of hours spent on studying and the mean mark obtained by the students in the class
Hour = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
Mark = np.array([50, 55, 60, 61, 68, 70, 71, 80, 84])

# Create the scatter plot using plt.scatter()
plt.scatter(Hour, Mark)

# Add axis labels and a title
plt.xlabel("No. of study hour")
plt.ylabel("Mean Mark obtained by a class")
plt.title("Students Mean mark and the number of hours spent on studying")

# Display the plot
plt.show()





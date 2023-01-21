# Activity 2 - Task 5
# Use of fill_between
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y1, label='y1')
ax.plot(x, y2, label='y2')

# Fill the area between the two lines
ax.fill_between(x, y1, y2, where=(y1 > y2), interpolate=False, color='gray')

# Add labels and a legend
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# Show the plot
plt.show()




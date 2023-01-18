# Activity 2 - Task 3 & 4
import numpy as np

# Create a 2-dimensional array with the points A, B, C
points = np.array([[0, 30], [-30, -30], [30, -30]])

# Indexing the point A
print("A:", points[0])
# Output: A: [ 0 30]

# Indexing the point B
print("B:", points[1])
# Output: B: [-30 -30]

# Indexing the point C
print("C:", points[2])
# Output: C: [30 -30]

# Slicing the x coordinates of all points
print("X coordinates:", points[:, 0])  # Output: X coordinates: [ 0 -30  30]

# Slicing the y coordinates of all points
print("Y coordinates:", points[:, 1])  # Output: Y coordinates: [ 30 -30 -30]




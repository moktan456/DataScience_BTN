# Activity 2 - Task 7
# Using histogram
import matplotlib.pyplot as plt

# Exam scores
scores = [65, 72, 80, 59, 93, 80, 75, 68, 55, 85, 60, 84, 70, 76, 86]

# Create histogram
plt.hist(scores, bins=10)
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Exam Scores Histogram')

# Show histogram
plt.show()




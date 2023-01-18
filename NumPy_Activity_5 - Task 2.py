# Activity 5 - Task 2 (Finding mean and median for the given set of data)
import numpy as np

# Test score data
scores = np.array([55,67,85,45,79,63,92,80,76,35])

# Finding the mean score

#mean_score = round(scores.mean(),1)

# or

mean_score = round(np.mean(scores),1)

print(f"The mean score is : {mean_score}")


# Finding the median score

med_score = np.median(scores)
print(f"The median score is : {med_score}")









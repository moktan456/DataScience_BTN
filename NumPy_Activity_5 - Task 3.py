# Activity 5 - Task 3 (Finding range, standard deviation and variance for
# the given set of data)
import numpy as np

# Test score data
scores = np.array([55,67,85,45,79,63,92,80,76,35])

# Finding the range


data_range = np.ptp(scores)

print(f"The range value is : {data_range}")


# Finding the standard deviation

data_std = round(np.std(scores),1)
print(f"The standard deviation is : {data_std}")

# Finding the variance

data_var = round(np.var(scores),1)

print(f"The variance is : {data_var}")





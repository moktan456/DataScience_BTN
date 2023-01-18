# Activity 5 - Task 4 (Finding Q1, Q2, and Q3)
import numpy as np

# Test score data
scores = np.array([55,67,85,45,79,63,92,80,76,35])
#scores = np.sort(values)
# Computing Q1 (lower quartile)


Q1 = np.quantile(scores,0.25)

print(f"The lower quartile Q1 is : {Q1}")


# Computing Q2 (inter quartile)


Q2 = np.quantile(scores,0.5)

print(f"The inter quartile Q2 is : {Q2}")

# Computing Q3 (upper quartile)


Q3 = np.quantile(scores,0.75)

print(f"The upper quartile Q3 is : {Q3}")





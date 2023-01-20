# Activity 2 - Task 5
# Using fill_between function
import matplotlib.pyplot as plt
import numpy as np

x = ['English','Dzongkha','Math','Science','History','Geography']
std1 = np.array([67,75,83,66,55,82])
std2 = np.array([75,66,34,89,59,94])

fig, ax = plt.subplots()
ax.plot(x,std1, label = 'std_1')
ax.plot(x,std2, label = 'std_2')

ax.fill_between(x,std1,std2, where=(std1>std2),interpolate=False, color='green')

ax.set_xlabel('Subject')
ax.set_ylabel('Score')
ax.legend()

plt.show()



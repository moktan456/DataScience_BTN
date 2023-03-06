import numpy as np
import matplotlib.pyplot as plt

std_name = ['Karma','Nima','Sonam','Pema','Kinley']

ca = np.array([8.5,9,8,7,8.8])
exam = np.array([38,45.5,40,39,35])

total = np.add(ca, exam)

# Creating a bar chart or plot

plt.bar(std_name, total)
plt.xlabel('Student name')
plt.ylabel('Total marks')
plt.title('Total marks obtained')

plt.show()

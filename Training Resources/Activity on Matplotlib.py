import numpy as np
import matplotlib.pyplot as plt

std_name = ['Nima','Karma','Sonam']
marks = np.array([45,56,67])

plt.bar(std_name, marks)

plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.title('Marks obtained by students')
plt.show()

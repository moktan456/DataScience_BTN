
import matplotlib.pyplot as plt
import numpy as np
#Creating the array using numpy
student_name = np.array(['Karma', 'Tshering', 'Sonam', 'Pema', 'Kinley'])
ca = np.array([8.5, 9, 8, 7, 8.5])
exam = np.array([38, 45.5, 40, 39, 35])
#Adding CA and Exam Marks together
total = np.add(ca, exam)
#Drawing bar graph to dispaly the data
plt.bar(student_name, total)
plt.xlabel("Name of the students")
plt.ylabel("Total marks")
plt.title('Total marks secured by 5 students ')
plt.show()



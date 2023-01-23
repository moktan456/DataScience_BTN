
import matplotlib.pyplot as plt

classes = ['class I','class II', 'class III', 'class IV']
male = [23, 16, 19, 17]
female = [19, 21, 18, 23]

fig, ax = plt.subplots(1,1)
ax.plot(classes,male)
ax.plot(classes,female)
plt.xlabel('Classes')
plt.ylabel('Number of Male and Female students in each class')
plt.title('Number of Students by Gender in Four Classes')

plt.show()




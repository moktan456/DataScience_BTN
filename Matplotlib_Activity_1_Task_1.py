import matplotlib.pyplot as plt

mass = [0, 2, 4, 6, 8, 10]
length = [15.0, 13.2, 11.4, 9.6, 7.8, 6.0]

# Creating the scatter plot 
plt.scatter(mass, length)
plt.xlabel('Mass added (kg)')
plt.ylabel('Length of spring (cm)')

plt.show()

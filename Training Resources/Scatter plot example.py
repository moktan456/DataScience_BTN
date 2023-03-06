import matplotlib.pyplot as plt

mass = [0,2,4,6,8,10]
length = [15,13.2,11.4,9.6,7.8,6]

# Create a scatter plot
plt.scatter(mass,length)
plt.xlabel('Mass in Kg')
plt.ylabel('Length of the spring in cm')
plt.title('Science experiment data')

plt.show()

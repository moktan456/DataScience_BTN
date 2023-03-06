import matplotlib.pyplot as plt

activities = ['Reading','TV','Games','Song and Dance', 'Others']
time = [5.56,70.56,15.45,5.567,5.4567]

# Create pie chart

plt.pie(time, labels = activities, autopct = '%.2f%%')
plt.title('Time spent in activities')

plt.show()


import matplotlib.pyplot as plt

activities = ['Reading','TV','Games', 'Song and dance', 'Others']
time = [5, 70, 15, 5, 5]

# Create a pie chart
plt.pie(time, labels =activities, autopct='%1.1f%%')
plt.title('Percent of Time Teens in a School in Thimphu Spend on Leisure Activities')

# Show chart
plt.show()



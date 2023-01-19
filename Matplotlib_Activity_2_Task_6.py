# Activity 2 - Task 6
# Use of pie chart
import matplotlib.pyplot as plt

# Number of students playing each sport
sports = ['Football', 'Basketball', 'Tennis', 'Volleyball', 'Soccer']
no_of_students = [35, 25, 20, 15, 5]

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(no_of_students, labels = sports, autopct='%1.1f%%')
ax.set_title('Number of Students Playing Different Sports')

# Show chart
plt.show()




# Activity 2 - Task 4
import matplotlib.pyplot as plt

# Sample data
hours = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00",
         "06:00", "07:00", "08:00","09:00", "10:00", "11:00",
         "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
         "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
counts = [100, 50, 20, 10, 5, 20, 50, 80, 120, 150, 200, 250,
          300, 250, 200, 150, 120, 80, 50, 30, 20, 15, 10, 5]

# Create the step function plot
fig, ax = plt.subplots()
ax.step(hours, counts, where='post')
ax.set_xlabel('Hour')
ax.set_ylabel('Pedestrian Count')

plt.show()






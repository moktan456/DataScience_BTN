#Activity_2_Task_3
import matplotlib.pyplot as plt
import numpy as np

# Create data for the date and number of patients who have visited the hospital on that day
date = ['02-01-23', '03-01-23', '04-01-23', '05-01-23','06-01-23','07-01-23','08-01-23']
No_of_patient = [2000, 1500, 5200, 3150, 1760, 956, 2975]

# Create the stem plot using plt.stem()
plt.stem(date, No_of_patient, '-.')

# Add axis labels and a title
plt.xlabel("Date")
plt.ylabel("No.of patient")
plt.title("No. of people visited Thimphu Hospital in the first week of January")

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Display the plot
plt.show()




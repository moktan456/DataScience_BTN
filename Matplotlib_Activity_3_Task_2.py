
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Tourist_Arrival_2018.csv')
plt.stem(data['Country'], data['Total'],
         linefmt = '-.', markerfmt = 'o', basefmt = 'c-')


plt.xlabel('Name of Coutries')
plt.xticks(rotation = 90)
plt.ylabel('Total Tourist')
plt.title('Total Tourist arrival in 2018')
plt.show()





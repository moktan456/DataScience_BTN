import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Tourist_Arrival_2018.csv')

plt.hist(data['Total'], bins = 10, color = 'c')

plt.xlabel('Range')
plt.xticks(rotation = 90)
plt.ylabel('Frequency')
plt.title('Distribution of Tourist')
plt.show()


"""
plt.stem(data['Country'], data['Total'], linefmt = '-.', markerfmt = 'o', basefmt = 'r-')

plt.xlabel('Various Coutries')
plt.xticks(rotation = 90)
plt.ylabel('Total Number')
plt.title('Tourist arrival in January Month')
plt.show()

"""





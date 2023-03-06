import matplotlib.pyplot as plt

sizes = [20.1234, 30.345, 50.456]
labels = ['Apples', 'Bananas', 'Oranges']

plt.pie(sizes, labels=labels, autopct='%.1f%%')

plt.show()

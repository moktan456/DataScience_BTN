import pandas as pd

# Read a CSV file of Tourist arrival of 2018 in Bhutan
df = pd.read_csv('Tourist_Arrival_2018.csv')

# Sort the DataFrame by Total in descending order
sort = df.sort_values(by='Total', ascending=False)

print('\n*****Statistics of Top 10 countries that visited Bhutan*****')
print(sort.head(10))

print('\n*****Statistics of Top 15 to 20 countries that visited Bhutan*****')
print(sort.tail())




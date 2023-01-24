import pandas as pd

# Read a CSV file of Tourist arrival of 2018 in Bhutan
df = pd.read_csv('Tourist_Arrival_2018.csv')

# Print the maximum number of Total column
print('\n*****Maximum total number of Tourist arrived*****')
print(df['Total'].max())

# Print the Minimum number of Total column
print('\n*****Lowest total number of Tourist arrived*****')
print(df['Total'].min())


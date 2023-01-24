import pandas as pd

# Read a CSV file of Tourist arrival of 2018 in Bhutan
df = pd.read_csv('Tourist_Arrival_2018.csv')

# Print description of the data
print('*****Statistical information on the content*****')
print(df.describe())


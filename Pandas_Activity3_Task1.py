import pandas as pd

# Read a CSV file of Tourist arrival of 2018 in Bhutan
df = pd.read_csv('Tourist_Arrival_2018.csv')

# Sort the DataFrame by Total in descending order
sort = df.sort_values(by='Total', ascending=False)

# Print description of the data
print('*****Information about the file*****')
print(df.info())



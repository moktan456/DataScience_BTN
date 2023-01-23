import pandas as pd

# Read a CSV file of Tourist arrival of 2018 in Bhutan
df = pd.read_csv('Tourist_Arrival_2018.csv')

# Print Tourist_Arrival_2018 file in the DataFrame
print(df)

# Print 2 new line 
print('\n\n')

# Sort the DataFrame by Total in descending order
sort = df.sort_values(by='Total', ascending=False)

print('\n\n')
print('*****Statistics of Top 10 countries that visited Bhutan*****')
print(sort.head(10))

print('\n\n')
print('*****Statistics of Top 15 to 20 countries that visited Bhutan*****')
print(sort.tail())

print('\n\n')
# Print description of the data
print('*****Statistical information on the content*****')
print(df.describe())

print('\n\n')
# Print the maximum number of Total column
print('*****Maximum total number of Tourist arrived*****')
print(df['Total'].max())
 
print('\n\n')
# Print the Minimum number of Total column
print('*****Lowest total number of Tourist arrived*****')
print(df['Total'].min())

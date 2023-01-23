import pandas as pd

# Read a CSV file
data = pd.read_csv('BHSC_2021_Sub_Performance.csv')

# Print Dataset
print(data)
print('\n')


#Print new column with addtion of Female & Male 
data['Total_Appeared'] = data['Female'] + data['Male']
print(data)
print('\n')

# Find Average of all the columns with numerical values
print('*****Average of all numeric data*****')
allRow_col4_7 = data.iloc[0:15,3:8]
ave_data = allRow_col4_7.mean()
print(ave_data)
print('\n')

# Find middle value in the PASS% column
print('*****Median of PASS%*****')
median_Pass_Percent = data['PASS%'].median()
print(median_Pass_Percent)
print('\n')

# Look for the value that appears most frequently
print('*****Mode of Total Students*****')
mode_Pass_Percent = data['Total_Appeared'].mode()
print(mode_Pass_Percent)
print('\n')

# Calculate how far apart the values in a dataset are from the mean
print('*****Standard Deviation of PASS%*****')
std_Pass_Percent = data['PASS%'].std()
print(std_Pass_Percent)

print('\n')


"""
# Print new information which is sum of total
sum_of_total = data['Total_Appeared']
total =sum_of_total.sum()
print("Sum of Total Appeared: ", total)
print('\n')
"""

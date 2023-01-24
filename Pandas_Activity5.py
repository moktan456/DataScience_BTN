import pandas as pd

# Read a CSV file
data = pd.read_csv('BHSC_2021_Sub_Performance.csv')

#Print new column with addtion of Female & Male 
data['Total_Appeared'] = data[['Female','Male']].sum(axis = 1)
print('\n1. Total students who appeared for each subject are: \n', data)

# Print new information which is sum of total
sum_of_total = data['Total_Appeared']
total =sum_of_total.sum()
print('\n2. Total numbers of papers written by all students together : ', total)

# Find Average of all the columns with numerical values
allRow_col4_7 = data.iloc[0:15,3:8]
ave_data = allRow_col4_7.mean().round(2)
print('\n3. Average of all numeric data is : ', ave_data)

# Find middle value in the PASS% column
median_Pass_Percent = data['PASS%'].median().round(2)
print('\n4. Median of PASS% is : ', median_Pass_Percent)

# Look for the value that appears most frequently
mode_Pass_Percent = data['Total_Appeared'].mode()
subject_mode = data[data['Total_Appeared'].isin(mode_Pass_Percent)]
print('\n5. Mode of Total Students is : \n', subject_mode)

# Calculate how far apart the values in a dataset are from the mean
std_Pass_Percent = data['PASS%'].std()
rounded_std_Pass_Percent = std_Pass_Percent.round(2)
print('\n6. Standard Deviation of PASS%', rounded_std_Pass_Percent)

# Check the relationship stranght between CA, Theory and final Pass
cor_CA_PASS = data['CA Pass'].corr(data['PASS']).round(2)
cor_TH_PASS = data['TH Pass'].corr(data['PASS']).round(2)
print("\n7i. Correlation between 'CA' & 'PASS' is : ", cor_CA_PASS)
print("\n7ii. Correlation between 'TH' & 'PASS' is : ",cor_TH_PASS)



import pandas as pd

data = pd.read_csv('Exercise_Record.csv')

# Print dataset
print(data)
print('\n')

# Inserting missing date at index 22
data.loc[22, 'Date'] = '2020/12/22'

# Converting all cells in the 'Date' column into dates
data['Date'] = pd.to_datetime(data['Date'])

# Collecting Edited row 20 to 30 of Date column 
r20_30_c2 = data.iloc[19:29, 1]
print(r20_30_c2)
print('\n')




# Collecting all data with non-null values under Calories
calories_notna = data[data["Calories"].notna()]
print(calories_notna)
print('\n')

# Determining all data of maximum calories burnt
max_calories_burnt = data.loc[data["Calories"]>=350]
print(max_calories_burnt)
print('\n')

# Collecting dates when maximum calories were burnt
date_max_Calories_burnt = data.loc[data["Calories"]>=350, "Date"]
print(date_max_Calories_burnt)

print('\n')
# filter data using isin()
filtered_data = data[data["Duration"].isin([45])]

# display filtered data
print('*****Exercise Record with Duration of 45 minutes*****') 
print(filtered_data)


# save filtered data
filtered_data.to_csv("filtered_data.csv", index=False)


print('\n')

# check shape of data
print('*****Original shape of data*****')
print(data.shape)

# drop missing values
data = data.dropna()

# check shape after dropping missing values
print('*****Data shape after removing null values*****')
print(data.shape)

# remove duplicates
data = data.drop_duplicates()

# check shape after removing duplicates
print('*****Data shape after removing duplicate values*****')
print(data.shape)




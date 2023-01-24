import pandas as pd

data = pd.read_csv('Exercise_Record.csv')

# check shape of data
print('\n*****Original shape of data*****')
print(data.shape)

# drop missing values
data = data.dropna()

# check shape after dropping missing values
print('\n*****Data shape after removing null values*****')
print(data.shape)

# remove duplicates
data = data.drop_duplicates()

# check shape after removing duplicates
print('\n*****Data shape after removing duplicate values*****')
print(data.shape)




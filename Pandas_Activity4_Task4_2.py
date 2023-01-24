import pandas as pd

data = pd.read_csv('Exercise_Record.csv')

# Inserting missing date at index 22
data.loc[22, 'Date'] = '2020/12/22'

# Converting all cells in the 'Date' column into dates
data['Date'] = pd.to_datetime(data['Date'])

# Collecting Edited row 20 and below of Date column 
r20_c1 = data.iloc[20:, 1]
print(r20_c1)




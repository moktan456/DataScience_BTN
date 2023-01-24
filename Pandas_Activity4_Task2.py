import pandas as pd

data = pd.read_csv('Exercise_Record.csv')

# filter data using isin()
filtered_data = data[data["Duration"].isin([30])]

# display filtered data
print('\n*****Exercise Record with half the Duration*****') 
print(filtered_data)





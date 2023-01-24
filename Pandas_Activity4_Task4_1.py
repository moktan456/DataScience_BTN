import pandas as pd

data = pd.read_csv('Exercise_Record.csv')

# Collecting Edited row 20 and below of Date column 
r20_c1 = data.iloc[20:, 1]
print(r20_c1)




import pandas as pd

data = pd.read_csv('Exercise_Record.csv')

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



import pandas as pd

# Create a data frame with Bhutanese population data
data = {'Dzongkhag': ['Thimphu', 'Punakha', 'Wangdue Phodrang', 'Trashigang', 'Bumthang'],
        'Population': [114551, 6262, 8954, 2383, 17820],
        'Land Area': [1426, 1110, 4308, 3066, 2717]}
df = pd.DataFrame(data)

# Add a column for population density
df['Density'] = df['Population'] / df['Land Area']

# Print the updated data frame
print(df)

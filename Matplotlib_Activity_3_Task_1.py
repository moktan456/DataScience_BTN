import pandas as pd
import matplotlib.pyplot as plt

# Create a data frame with Bhutanese population data
data = {'Dzongkhag': ['Thimphu', 'Punakha', 'Wangdue Phodrang', 'Trashigang', 'Bumthang'],
        'Population': [114551, 6262, 8954, 2383, 17820],
        'Land Area': [1426, 1110, 4308, 3066, 2717]}
df = pd.DataFrame(data)

# Add a column for population density
df['Density'] = df['Population'] / df['Land Area']

# Print the updated data frame
print(df)
#Plot the scatter plot for Population and Density
plt.scatter(df['Dzongkhag'], df['Population'], label='Population')
plt.scatter(df['Dzongkhag'], df['Density'], label='Density')

plt.xlabel('Dzongkhag')
plt.ylabel('Population and Density')
plt.title('Bhutanese Population Data')
plt.legend()

plt.show()

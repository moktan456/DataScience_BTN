
import numpy as np


population = np.array([17820, 68966, 24965, 3952, 13655,
                   14437, 37150, 46316, 23632, 28740,
                   35079, 62590, 46004,138736, 17300,
                   45518, 19960, 22376, 42186, 17736])

Q1 = np.quantile(population,0.25)
print(f'The lower quartile Q1 is: {Q1}')

# Q2 is median
Q2 = np.quantile(population,0.5)
print(f'The lower quartile Q2 is: {Q2}')

Q3 = np.quantile(population,0.75)
print(f'The lower quartile Q3 is: {Q3}')






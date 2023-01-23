
import numpy as np


population = np.array([17820, 68966, 24965, 3952, 13655,
                   14437, 37150, 46316, 23632, 28740,
                   35079, 62590, 46004,138736, 17300,
                   45518, 19960, 22376, 42186, 17736])

min_pop = population.min()
print(f"The minimum population is : {min_pop}")



max_pop = population.max()
print(f"The maximum population is : {max_pop}")


range_pop = population.ptp()
print(f"The difference between min and max population is: {range_pop}")









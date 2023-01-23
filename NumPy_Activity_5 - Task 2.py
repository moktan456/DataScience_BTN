
import numpy as np


population = np.array([17820, 68966, 24965, 3952, 13655,
                   14437, 37150, 46316, 23632, 28740,
                   35079, 62590, 46004,138736, 17300,
                   45518, 19960, 22376, 42186, 17736])

mean_pop = round(np.mean(population),1)

print(f"The mean population is : {mean_pop}")


med_pop = np.median(population)
print(f"The median population is : {med_pop}")

var_pop = round(np.var(population),1)
print(f"The variance is : {var_pop}")

std_pop = round(np.std(population),1)
print(f"The standard deviation is: {std_pop}")







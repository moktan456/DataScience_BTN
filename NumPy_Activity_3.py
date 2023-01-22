
import numpy as np
A = np.array([(0.8,1,0.5),(1,0.9,0.6),(1,1,0.5)])
B = np.array([(0.3,1.2,0.7),(0.5,1.1,0.8),(0.5,1.3,0.7)])


if A.shape == B.shape:
    print("Matrices A and B can be added or subtracted")

print("\n")

sum_of_AB = A + B
print(f"Sum of A & B: \n {sum_of_AB}")

print("\n")

diff_of_AB = A - B
print(f"Difference of A & B: \n {diff_of_AB}")





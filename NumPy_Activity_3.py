# Activity 3 - Addition and Subtraction of Matrices
import numpy as np
A = np.array([(0.8,1,0.5),(1,0.9,0.6),(1,1,0.5)])
B = np.array([(0.3,1.2,0.7),(0.5,1.1,0.8),(0.5,1.3,0.7)])
# Check whether matrices A and B have same shape
# Both matrices should have same shape (dimension)

if A.shape == B.shape:
    print("Matrices A and B can be added or subtracted")


# Add the two matrices

sum_of_AB = A + B
print("A + B is: \n",sum_of_AB)

print("\n")

# Subtract two matrices
diff_of_AB = A - B
print("A - B is: \n", diff_of_AB)





# Activity 4 - Task 1
# Matrix multiplication using NumPy
import numpy as np
A = np.array([[80,70,77],[90,78,82],[75,85,87],[85,71,78]])
B = np.array([[0.3],[0.2],[0.5]])
# Check whether matrices A and B can be multiplied
# It should fulfill this condition [m * n] * [n * p] = [m * p]

rowA, colA = A.shape
rowB, colB = B.shape
if  colA == rowB:
    print("Matrices A and B can be multiplied")

# Product of two matrices
# Student's final grade

# Method 1
product_AB = A @ B

print(f"Student's final grade is: \n {product_AB}")

# Method 2

product_AB = A.dot(B)

print(f"Student's final grade is: \n {product_AB}")


# Method 2 - other way of using .dot

product_AB = np.dot(A,B)

print(f"Student's final grade is: \n {product_AB}")






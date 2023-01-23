
import numpy as np

A = np.array([[80,70,77],[90,78,82],[75,85,87],[85,71,78]])
B = np.array([[0.3],[0.2],[0.5]])

# Unpacking the tuple
rowA, colA = A.shape
rowB, colB = B.shape 

# Checking condition for matrix multiplication
if  colA == rowB:
    print("Matrices A and B can be multiplied")



product_AB = A @ B

print(f"Student's final grade is: \n {product_AB}")


product_AB = A.dot(B)

print(f"Student's final grade is: \n {product_AB}")










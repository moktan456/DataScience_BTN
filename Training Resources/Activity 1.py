import numpy as np

Day1 = [[0.8,1,0.5],[1,0.9,0.6],[1,1,0.5]]
Day2 = [[0.3,1.2,0.7],[0.5,1.1,0.8],[0.5,1.3,0.7]]

A = np.array(Day1)
B = np.array(Day2)

print("Dimension of A" ,A.shape)
print("No of elements in B", B.size)

print("Indexing: ", A[0,1])

print("Slicing: ", A[:,2])

print("Time spent on each subject: \n", A + B)

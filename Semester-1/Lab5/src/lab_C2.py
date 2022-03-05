# program to perform addition and subtraction of two matrices using numpy

import numpy as np

mat1 = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
])

mat2 = np.array([
    [0, 0, 0],
    [1, 2, 3],
    [4, 5, 6]
])


print("Addition :", mat1 + mat2, sep="\n")
print("Subtraction :", mat1 - mat2, sep="\n")

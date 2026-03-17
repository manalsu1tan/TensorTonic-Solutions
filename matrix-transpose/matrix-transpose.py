import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    arr = np.array(A)
    temp = np.zeros((arr.shape[1], arr.shape[0])) 
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            temp[j][i] = A[i][j]
    return temp

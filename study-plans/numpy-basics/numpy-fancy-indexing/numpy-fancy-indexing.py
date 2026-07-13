import numpy as np

def select_by_index(arr, indices, axis):
    """
    Returns: 2D ndarray of float64
    """
    a = np.array(arr, dtype=np.float64)
    return np.take(a, indices, axis=axis)
    
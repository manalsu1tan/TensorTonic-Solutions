import numpy as np

def scale_cols(data, weights):
    """Returns: np.ndarray of shape (m, n), each column scaled by corresponding weight"""
    A = np.array(data)
    w = np.array(weights)
    result = A * w
    return result
    
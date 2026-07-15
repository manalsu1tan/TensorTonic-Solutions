import numpy as np

def scale_rows(data, weights):
    """Returns: np.ndarray of shape (m, n), each row scaled by corresponding weight"""
    A = np.array(data)
    s = np.array(weights)
    return A * s[:, np.newaxis]
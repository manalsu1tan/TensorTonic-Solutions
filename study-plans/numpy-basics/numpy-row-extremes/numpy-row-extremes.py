import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""
    arr = np.array(data, dtype=np.float64)
    row_min = arr.min(axis=1)
    row_max = arr.max(axis=1)
    min_idx = arr.argmin(axis=1)
    max_idx = arr.argmax(axis=1)
    return np.stack([row_max, max_idx, row_min, min_idx])
import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    arr = np.array(data, dtype=np.float64)
    block = arr[row_idx, :]
    block2 = np.clip(block, lo, hi)
    return np.stack([block, block2])
    
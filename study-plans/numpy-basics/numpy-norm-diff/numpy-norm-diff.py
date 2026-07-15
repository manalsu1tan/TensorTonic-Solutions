import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    arr_a = np.array(a, dtype=np.float64)
    arr_b = np.array(b, dtype=np.float64)
    if lo is not None or hi is not None:
        arr_a = np.clip(arr_a, lo, hi)
        arr_b = np.clip(arr_b, lo, hi)

    a_scaled = (arr_a - lo) / (hi - lo)
    b_scaled = (arr_b - lo) / (hi - lo)
    return np.abs(a_scaled - b_scaled)
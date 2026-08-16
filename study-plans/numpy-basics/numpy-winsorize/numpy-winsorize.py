import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    arr = np.array(data, dtype=np.float64)
    lo = np.percentile(arr, lo_q, axis=0)
    hi = np.percentile(arr, hi_q, axis=0)
    clipped = np.clip(arr, lo, hi)
    clipped_lo = (arr < lo).astype(np.float64)
    clipped_hi = (arr > hi).astype(np.float64)
    return np.stack([clipped, clipped_lo, clipped_hi])
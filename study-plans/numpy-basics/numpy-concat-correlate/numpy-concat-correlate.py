import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""
    a_arr = np.array(a, dtype=np.float64)
    b_arr = np.array(b, dtype=np.float64)
    conc = np.concatenate([a, b], axis=0)
    a_corrcoef = np.corrcoef(a_arr.T)
    b_corrcoef = np.corrcoef(b_arr.T)
    a_b_corrcoef = np.corrcoef(conc.T)
    return np.stack([a_corrcoef, b_corrcoef, a_b_corrcoef])
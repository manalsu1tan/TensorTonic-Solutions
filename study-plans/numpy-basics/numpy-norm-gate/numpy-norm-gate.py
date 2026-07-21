import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    arr_X = np.array(X)
    arr_W = np.array(W)
    arr_Z = np.matmul(X, W)
    norms = np.linalg.norm(arr_Z, axis=1)
    gate = (norms >= threshold).astype(arr_Z.dtype)
    return arr_Z * gate[:, np.newaxis]
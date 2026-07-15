import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    arr = np.asarray(data)
    arr1 = np.where(arr > threshold, 1.0, 0.0)
    arr2 = np.where(np.any(arr > threshold, axis=1, keepdims=True), arr, 0.0)
    filtered2 = np.broadcast_to(arr2, arr.shape)
    arr3 = np.where(np.all(arr > threshold, axis=1, keepdims=True), arr, 0.0)
    filtered3 = np.broadcast_to(arr3, arr.shape)
    return np.stack([arr1, filtered2, filtered3])
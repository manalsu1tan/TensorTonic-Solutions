import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    arr = np.array(data, dtype=np.float64)
    dec = np.round(arr, decimals=decimals)
    dec_padded = np.pad(dec, pad_width, mode='constant', constant_values=0)
    floored = np.floor(arr)
    floored_padded = np.pad(floored, pad_width, mode='constant', constant_values=0)
    ceiled = np.ceil(arr)
    ceiled_padded = np.pad(ceiled, pad_width, mode='constant', constant_values=0)
    return np.stack([dec_padded, floored_padded, ceiled_padded])
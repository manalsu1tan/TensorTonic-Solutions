import numpy as np

def angle_features(angles):
    """Returns: np.ndarray of shape (3, n), rows are sin, cos, tan"""

    arr = np.array(angles)
    return np.stack([np.sin(angles), np.cos(angles), np.tan(angles)])
    
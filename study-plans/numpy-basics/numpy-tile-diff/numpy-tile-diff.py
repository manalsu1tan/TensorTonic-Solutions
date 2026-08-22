import numpy as np

def tile_diff(data, reps):
    """Returns: np.ndarray of shape (2, m*reps, n), stacked tiled array and padded differences"""
    arr = np.array(data, dtype=np.float64)
    tile = np.tile(arr, (reps, 1))
    diffs = np.diff(tile, axis=0)
    return np.stack([tile, np.pad(diffs, ((0, 1), (0, 0)))])
    
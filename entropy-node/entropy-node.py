import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    new_y = np.array(y)
    total_samples = len(new_y)
    unique_values, counts = np.unique(new_y, return_counts=True)
    num_classes = len(np.unique(new_y))
    new_arr = []
    for i in range(0, num_classes):
        p_i = counts[i] / total_samples
        h_s = p_i*np.log2(p_i)
        new_arr.append(h_s)
    return -np.sum(new_arr)
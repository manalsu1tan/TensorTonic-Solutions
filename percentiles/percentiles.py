import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    new_x = np.sort(np.array(x))
    new_q = np.sort(np.array(q))
    arr = []
    for i in new_q:
        if i == 0:
            arr.append(new_x[0])
        elif i == 100:
            arr.append(new_x[-1])
        else:
            idx = (len(new_x) - 1) * (i / 100)
            v_floor = int(np.floor(idx))
            v_ceil = int(np.ceil(idx))
            weight = idx % 1
            arr.append((1 - weight) * new_x[v_floor] + weight * new_x[v_ceil])
    return np.array(arr)
            
            
            
        
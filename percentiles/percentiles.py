import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    new_x = np.array(x)
    new_x = np.sort(new_x)
    new_q = np.array(q)
    new_q = np.sort(new_q)
    arr = []
    for i in q:
        if i == 0:
            arr.append(new_x[0])
        elif i == 100:
            arr.append(new_x[-1])
        else:
            idx = (len(new_x) - 1) * (i / 100)
            v_floor = np.floor(idx).astype(int) 
            v_ceil = np.ceil(idx).astype(int)
            lower = new_x[v_floor]
            upper = new_x[v_ceil]
            weight = idx % 1
            arr.append((1 - weight) * lower + weight * upper)
    return np.array(arr)
            
            
            
        
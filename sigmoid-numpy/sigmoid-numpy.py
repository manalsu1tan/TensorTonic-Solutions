import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    return (1 + np.exp(-np.array(x)))**-1
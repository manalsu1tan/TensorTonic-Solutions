import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x_t = torch.tensor(x, dtype=torch.float32)
    if op == "flatten":
        return x_t.flatten().tolist()
    elif op == "squeeze":
        return x_t.squeeze().tolist()
    elif op == "transpose":
        return x_t.transpose(0, 1).tolist()
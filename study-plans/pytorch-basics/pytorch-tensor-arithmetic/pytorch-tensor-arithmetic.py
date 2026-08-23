import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    x_t = torch.tensor(x, dtype=torch.float32)
    y_t = torch.tensor(y, dtype=torch.float32)
    
    if op == "add":
        return torch.add(x_t, y_t).tolist()
    elif op == "multiply":
        return torch.multiply(x_t, y_t).tolist()
    elif op == "matmul":
        return torch.matmul(x_t, y_t).tolist()
    elif op == "power":
        return torch.pow(x_t, y_t).tolist()
    elif op == "max":
        return torch.max(x_t, y_t).tolist()
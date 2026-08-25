import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    t = torch.tensor(x)
    if method == "relu":
        return torch.where(t > 0, t, 0).tolist()
    if method == "sigmoid":
        return (1 / (1 + torch.exp(-t))).tolist()
    if method == "tanh":
        return ((torch.exp(t) - torch.exp(-t)) / (torch.exp(t) + torch.exp(-t))).tolist()
    if method == "leaky_relu":
        return torch.where(t > 0, t, 0.01*t).tolist()
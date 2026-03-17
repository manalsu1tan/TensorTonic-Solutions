def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = a*(x0**2)+b*x0+c
    for i in range(steps):
        x = x - lr * (2 * a * x + b)
    return x
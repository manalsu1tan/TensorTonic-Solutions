from collections import deque
def discounted_returns(rewards, gamma):
    """
    Returns: list of G_t values, one per timestep, each rounded to 4 decimals
    """
    g_t_vals = deque()
    running_rew = 0.0
    for i in range(len(rewards) - 1, -1, -1):
        running_rew = running_rew * gamma + rewards[i] 
        g_t_vals.appendleft(running_rew)
    return [round(x, 4) for x in g_t_vals]
        
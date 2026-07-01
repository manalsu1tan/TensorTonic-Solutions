import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    mask = df[column] == old_val
    sum = mask.sum()
    df.loc[mask, column] = new_val
    return {"data": df.to_dict(orient="list"), "count": sum}
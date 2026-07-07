import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    df = pd.DataFrame(data)
    sum = df.groupby(group_col)[value_col].sum()
    mean = df.groupby(group_col)[value_col].mean()
    count = df.groupby(group_col)[value_col].count()
    return {"sum": sum.to_dict(), "mean": mean.to_dict(), "count": count.to_dict()}
    
    
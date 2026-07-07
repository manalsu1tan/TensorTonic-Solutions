import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    return pd.merge(pd.DataFrame(left), pd.DataFrame(right), how=how, on=on).to_dict(orient="list")
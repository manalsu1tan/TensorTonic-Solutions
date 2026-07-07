import pandas as pd

def unstack_to_wide(data, index_col, columns_col, values_col):
    """
    Returns: dict with index_col plus one key per unique value in columns_col
    """
    df = pd.DataFrame(data)
    wide = df.set_index([index_col, columns_col])[values_col].unstack()
    wide = wide.reset_index()
    return wide.to_dict(orient="list")
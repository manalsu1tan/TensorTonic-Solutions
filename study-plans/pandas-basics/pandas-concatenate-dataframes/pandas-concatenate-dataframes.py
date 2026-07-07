import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    df_list = [pd.DataFrame(df) for df in dfs]
    df = pd.concat(df_list, ignore_index=True)
    return [df.shape, df.to_dict(orient="list")]
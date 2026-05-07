import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    lis = [list(df.columns)]
    df = df.reset_index()
    lis.append(list(df.columns))
    return lis
import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    df = pd.DataFrame(data)
    new_col = column + "_transformed"
    if operation == "normalize":
        col_min = df[column].min()
        col_max = df[column].max()
        if col_min == col_max:
            df[new_col] = 0.0
        else:
           df[new_col] =((df[column] - col_min) / (col_max - col_min)).round(4)
    if operation == "rank":
        df[new_col] = df[column].rank(method="dense").astype(int)
    if operation == "cumsum":
        df[new_col] = df[column].cumsum()
    if operation == "double":
        df[new_col] = df[column] * 2

    return df.to_dict(orient="list")
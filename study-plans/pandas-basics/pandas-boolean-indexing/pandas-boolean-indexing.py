import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    mask = df[column] > threshold
    return {
        "filtered_data": df[mask].to_dict(orient="list"),
        "count": df[mask].shape[0]
    }
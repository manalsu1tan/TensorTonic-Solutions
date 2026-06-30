import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    df = pd.DataFrame(data)
    null_counts = df.isna().sum().to_dict()
    df = df.mask(df.isna(), fill_value)
    return {"null_counts": null_counts, "cleaned_data": df.to_dict(orient="list")}
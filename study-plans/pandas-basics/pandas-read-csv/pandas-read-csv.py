import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    df = pd.DataFrame(data=data)
    new_dict = {}
    new_dict["data"] = df.to_dict('list')
    new_dict["shape"] = list(df.shape)
    new_dict["columns"] = list(df.columns)
    
    return new_dict
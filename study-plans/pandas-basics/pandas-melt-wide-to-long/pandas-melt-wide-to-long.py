import pandas as pd

def melt_dataframe(data, id_vars, value_vars):
    """
    Returns: dict with keys from id_vars plus 'variable' and 'value'
    """
    return pd.melt(pd.DataFrame(data), id_vars, value_vars).to_dict(orient="list")
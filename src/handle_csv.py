import pandas as pd

def open_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df

def write_to_csv(df, result_path):
    df.to_csv(result_path)

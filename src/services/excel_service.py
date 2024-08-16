import pandas as pd

def read_excel_file(file_path):
    return pd.read_excel(file_path).to_dict(orient='records')

def write_excel_file(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

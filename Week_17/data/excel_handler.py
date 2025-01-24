import pandas as pd

def load_excel_data(excel_file):
    try:
        return pd.read_excel(excel_file)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Descripcion", "Categoria", "Tipo", "Monto"])

def save_data(data, excel_file):
    data.to_excel(excel_file, index=False)

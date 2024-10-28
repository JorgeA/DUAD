import pandas as pd
import os


# Ruta a excel
CATEGORIES_FILE = r"C:\Users\jarg0317\OneDrive - Sysco Corporation\Documents\DUAD\Week_17\data\categories.xlsx"

def load_data(excel_file):
    # Verifique si el archivo Excel existe; si no existe, cree uno.
    if not os.path.exists(excel_file):
        create_empty_transactions_file(excel_file)

    try:
        # Lee el contenido del file
        df = pd.read_excel(excel_file, engine='openpyxl')
        return df.values.tolist()
    except Exception as e:
        print(f"Error loading data: {e}")
        return []


def create_empty_transactions_file(excel_file):
    """Creates an empty Excel file with the required structure."""
    df = pd.DataFrame(columns=["Descripcion", "Categoria", "Tipo", "Monto"])
    df.to_excel(excel_file, index=False, engine='openpyxl')


def save_data(data, excel_file):
    df = pd.DataFrame(data, columns=["Descripcion", "Categoria", "Tipo", "Monto"])
    df.to_excel(excel_file, index=False, engine='openpyxl')


def load_categories():
    # Verifica si la categoria existe, sino solicita crearla
    if not os.path.exists(CATEGORIES_FILE):
        create_empty_categories_file()

    try:
        df = pd.read_excel(CATEGORIES_FILE, engine='openpyxl')
        return df["Categoria"].tolist()
    except Exception as e:
        print(f"Error loading categories: {e}")
        return []


def create_empty_categories_file():
    """Creates an empty categories Excel file."""
    df = pd.DataFrame(columns=["Categoria"])
    df.to_excel(CATEGORIES_FILE, index=False, engine='openpyxl')


def save_category(category):
    categories = load_categories()
    if category in categories:
        raise ValueError(f"La categoria '{category}' ya existe.")
    categories.append(category)
    df = pd.DataFrame(categories, columns=["Categoria"])
    df.to_excel(CATEGORIES_FILE, index=False, engine='openpyxl')

def add_transaction(description, category, transaction_type, amount, excel_file):
    if category not in load_categories():
        raise ValueError(f"La categoria '{category}' no existe.")
    data = load_data(excel_file)
    data.append([description, category, transaction_type, float(amount)])
    save_data(data, excel_file)

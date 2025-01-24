import pandas as pd
import os

# Directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Obtiene la ruta del archivo actual

# Rutas relativas a la carpeta de datos
CATEGORIES_FILE = os.path.join(BASE_DIR, '..', 'data', 'categories.xlsx')
TRANSACTIONS_FILE = os.path.join(BASE_DIR, '..', 'data', 'finanzas.xlsx')

def load_data(excel_file=TRANSACTIONS_FILE):
    if not os.path.exists(excel_file):
        create_empty_transactions_file(excel_file)

    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        return df.values.tolist()
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def create_empty_transactions_file(excel_file):
    df = pd.DataFrame(columns=["Descripcion", "Categoria", "Tipo", "Monto"])
    df.to_excel(excel_file, index=False, engine='openpyxl')

def save_data(data, excel_file=TRANSACTIONS_FILE):
    df = pd.DataFrame(data, columns=["Descripcion", "Categoria", "Tipo", "Monto"])
    df.to_excel(excel_file, index=False, engine='openpyxl')

def load_categories():
    if not os.path.exists(CATEGORIES_FILE):
        create_empty_categories_file()

    try:
        df = pd.read_excel(CATEGORIES_FILE, engine='openpyxl')
        return df["Categoria"].tolist()
    except Exception as e:
        print(f"Error loading categories: {e}")
        return []

def create_empty_categories_file():
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

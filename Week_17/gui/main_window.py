import PySimpleGUI as sg
import os
from functions.logic import load_data, save_category, load_categories
from gui.add_transaction import open_transaction_window

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.path.join(BASE_DIR, "data", "finanzas.xlsx")

def launch_main_window():
    data = load_data(EXCEL_FILE)

    layout = [
        [sg.Table(values=data, headings=["Descripcion", "Categoria", "Tipo", "Monto"],
                  key="TABLE", auto_size_columns=True, num_rows=10)],
        [sg.Button("Agregar Categoria"), sg.Button("Agregar Gasto"), sg.Button("Agregar Ingreso")],
    ]

    window = sg.Window("Gestion de Finanzas Personales", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Agregar Categoria":
            category = sg.popup_get_text("Nueva Categoria")
            if category:
                try:
                    save_category(category)
                    sg.popup(f"Categoria '{category}' agregada.")
                except ValueError as e:
                    sg.popup_error(str(e))
        elif event == "Agregar Gasto":
            open_transaction_window(EXCEL_FILE, "Gasto")
            window["TABLE"].update(values=load_data(EXCEL_FILE))  # Refreshes main window table
        elif event == "Agregar Ingreso":
            open_transaction_window(EXCEL_FILE, "Ingreso")
            window["TABLE"].update(values=load_data(EXCEL_FILE))  

    window.close()

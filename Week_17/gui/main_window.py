import PySimpleGUI as sg
from functions.logic import load_data, save_category, load_categories
from gui.add_transaction import open_transaction_window

EXCEL_FILE = r"C:\Users\jarg0317\OneDrive - Sysco Corporation\Documents\DUAD\Week_17\data\finanzas.xlsx"

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
            window["TABLE"].update(values=load_data(EXCEL_FILE))  #Refresca la tabla del main window
        elif event == "Agregar Ingreso":
            open_transaction_window(EXCEL_FILE, "Ingreso")
            window["TABLE"].update(values=load_data(EXCEL_FILE))  

    window.close()

import PySimpleGUI as sg
from functions.logic import add_transaction

def open_transaction_window(excel_file, transaction_type):
    layout = [
        [sg.Text("Descripcion"), sg.Input(key="DESCRIPTION")],
        [sg.Text("Categoria"), sg.Input(key="CATEGORY")],
        [sg.Text("Monto"), sg.Input(key="AMOUNT")],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]

    window = sg.Window(f"Agregar {transaction_type}", layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        elif event == "Guardar":
            try:
                description = values["DESCRIPTION"]
                category = values["CATEGORY"]
                amount = float(values["AMOUNT"])
                add_transaction(description, category, transaction_type, amount, excel_file)
                sg.popup("Transaccion guardada.")
                break
            except ValueError as e:
                sg.popup_error(f"Error: {str(e)}")
            except Exception as e:
                sg.popup_error(f"Error inesperado: {str(e)}")

    window.close()

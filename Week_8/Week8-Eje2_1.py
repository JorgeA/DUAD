import csv


data = [
    {'nombre': 'Grand Theft Auto IV', 'genero': 'Accion', 'desarrollador': 'Rockstar Games', 'clasificacion': 'M'},
    {'nombre': 'The Elder Scrolls IV: Oblivion', 'genero': 'RPG', 'desarrollador': 'Bethesda', 'clasificacion': 'M'},
    {"nombre": "Tony Hawk's Pro Skater 2", 'genero': 'Deportes', 'desarrollador': 'Activision', 'clasificacion': 'T'}
]

headers = data[0].keys()

def crea_csv(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file,headers, dialect= 'excel-tab')
        writer.writeheader()
        writer.writerows(data)


crea_csv('example_csv.csv', data, headers)
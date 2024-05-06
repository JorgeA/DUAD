import csv
from actions import students


students_headers = (
            'name', 
            'group',
            'spanish_score',
            'english_score',
            'scienses_score',
            'social_studies_score',
            'score_avg'
            )

def export_students_csv(file_path, data, headers = students_headers):
    try:

        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(data)
        print("Students succesfully Exported to a CSV file...!!")
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')


def import_students(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key in row:
                    if key != 'name' and key != 'group':  # Excluimos 'name' y 'group'
                        row[key] = float(row[key])
                students.append(row)
        print(" ")
        print("Students Successfully Imported!!!")
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
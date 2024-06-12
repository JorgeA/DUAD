import csv
from actions import students
from actions import Student

students_headers = (
    'name', 
    'group',
    'spanish_score',
    'english_score',
    'sciences_score',
    'social_studies_score',
    'score_avg'
)

def student_to_dict(student):
    return {
        'name': student.name,
        'group': student.group,
        'spanish_score': student.spanish_score,
        'english_score': student.english_score,
        'sciences_score': student.sciences_score,
        'social_studies_score': student.social_studies_score,
        'score_avg': student.score_avg
    }

def export_students_csv(file_path, students, headers=students_headers):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows([student_to_dict(student) for student in students])
        print("Students successfully exported to a CSV file...!!")
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')


def import_students_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    name=row['name'],
                    group=row['group'],
                    spanish=int(row['spanish_score']),
                    sciences=int(row['sciences_score']),
                    social=int(row['social_studies_score']),
                    english=int(row['english_score'])
                )
                students.append(student)
        print("Students successfully imported from CSV file...!!")
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
students = []

class Student:

    def __init__(self, name, group, spanish,sciences,social, english):
        self.name = name
        self.group = group
        self.spanish_score = spanish
        self.sciences_score = sciences
        self.social_studies_score = social
        self.english_score = english
        self.score_avg = self.calculate_average()
        print("Student created sucessfully")
    

    def calculate_average(self):
        return (self.spanish_score + self.sciences_score + self.social_studies_score + self.english_score) / 4


def validate_score(score):
    while True:
        if not score.isdigit():
            print("Por favor ingrese una nota valida. Sin letras")
        else:
            score = int(score)
            if 0 <= score <= 100:
                return score
            else:
                print("Por favor ingrese una nota valida entre 0 y 100")
        score = input("Ingrese la nota correcta: ")


def create_student():
    name = input("Ingrese el nombre del estudiante: ")
    group = input("Ingrese el grupo del estudiante: ")
    spanish = validate_score(input("Ingrese la calificación de Español: "))
    science = validate_score(input("Ingrese la calificación de Ciencias: "))
    social = validate_score(input("Ingrese la calificación de Sociales: "))
    english = validate_score(input("Ingrese la calificación de Ingles: "))
    student = Student(name, group, spanish, science, social, english)
    students.append(student)
    print("Student created successfully")


def show_all_students():
    if not students:
        print("No hay estudiantes en la lista.")
        return

    for student in students:
        print(f"Nombre: {student.name} - Grupo: {student.group} - Español: {student.spanish_score} - Ciencias: {student.sciences_score} - Sociales: {student.social_studies_score} - Inglés: {student.english_score} - Score Average: {student.score_avg}")
        print(" ")



def show_top_score_avg():
    try:
        sorted_students = sorted(students, key=lambda x: x.score_avg, reverse=True)
        top_3 = sorted_students[:3]
        print("This is our TOP 3 STUDENTS!!!")
        print(" ")
        for student in top_3:
            print(f"Nombre: {student.name} - Score Average: {student.score_avg}")
            print(" ")
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')


def show_general_avg_score():
    try:
        all_students_avg = 0
        for student in students:
            all_students_avg += student.score_avg
        total = all_students_avg / len(students)
        print(f"The general score average for all the students is: {total}")
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
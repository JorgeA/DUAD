students = []

class Student:

    def __init__(self, name, group, spanish,scienses,social, english):
        self.name = name
        self.group = group
        self.spanish_score = spanish
        self.scienses_score = scienses
        self.social_studies_score = social
        self.english_score = english
        print("Student created sucessfully")


def create_student():
    name = input("Ingrese el nombre del estudiante: ")
    group = input("Ingrese el grupo del estudiante: ")
    spanish = int(input("Ingrese la calificación de Español: "))
    science = int(input("Ingrese la calificación de Ciencias: "))
    social = int(input("Ingrese la calificación de Sociales: "))
    english = int(input("Ingrese la calificación de Inglés: "))
    student = Student(name, group, spanish, science, social, english)
    students.append(student)


def show_all_students():
    for student in students:
        print(f"Nombre: {student.name} - Grupo: {student.group} - Español: {student.spanish_score} - Ciencias: {student.scienses_score} - Sociales: {student.social_studies_score} - Inglés: {student.english_score}")
        print(" ")

create_student()
show_all_students()
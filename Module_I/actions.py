students = []

def add_student():
    while True:
        try:
            student = {}
            student["name"] = input("Nombre completo del estudiante: ")
            student["group"] = input("Numero de Seccion del estudiante: ")
            student["spanish_score"] = validate_score(input("Ingrese la nota de Español: "))
            student["english_score"] = validate_score(input("Ingrese la nota de Ingles: "))
            student["scienses_score"] = validate_score(input("Ingrese la nota de Ciencias: "))
            student["social_studies_score"] = validate_score(input("Ingrese la nota de Estudios Sociales: "))
            student["score_avg"] = (
                int(student["spanish_score"]) + 
                int(student["english_score"]) + 
                int(student["social_studies_score"]) + 
                int(student["scienses_score"])
            ) / 4
            print("\nEstudiante agregado satisfactoriamente!!")
            students.append(student)
            break
        except ValueError as error:
            print(f'Ha ocurrido un error: {error}')
            print("Ingrese una nota en formato valido")
            break


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


def show_all_students():
    print(students)


def show_top_score_avg():
    try:
        sorted_students = sorted(students, key=lambda x: x['score_avg'], reverse=True)
        top_3 = sorted_students[:3]
        print("This is our TOP 3 STUDENTS!!!")
        print(" ")
        for student in top_3:
            print (student['name'])
            print (student['score_avg'])
            print(" ")
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')


def show_general_avg_score():
    try:
        all_students_avg = 0
        for student in students:
            all_students_avg += student["score_avg"]
        total = all_students_avg / len(students)
        print(f"The general score average for all the students is: {total}")
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
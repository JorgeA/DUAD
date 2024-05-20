students = []


def add_student():
    while True:
        try:
            student = {}
            student["name"]=input("Student's full name: ")
            student["group"]=input("Student's group number: ")
            student["spanish_score"]=int(input("Student's spanish score: "))
            student["spanish_score"]=validate_score(student["spanish_score"])
            student["english_score"]=int(input("Student's english score: "))
            student["english_score"]=validate_score(student["english_score"])
            student["scienses_score"]=int(input("Student's sciences score: "))
            student["scienses_score"]=validate_score(student["scienses_score"])
            student["social_studies_score"]=int(input("Student's social studies score: "))
            student["social_studies_score"]=validate_score(student["social_studies_score"])
            student["score_avg"]= (int(student["spanish_score"])+int(student["english_score"])+int(student["social_studies_score"])+int(student["scienses_score"])) /4
            print("")
            print("Student successfully added!!")
            students.append(student)
            break
        except ValueError as error:
            print(f'Ha ocurrido un error: {error}')
            print("Ingrese una nota en formato valido")
            error_field = str(error).split("'")[1]
            #student[error_field] = int(input(f"Corrija el valor de {error_field} por una nota valida: "))
            #students.append(student)
            #break
def validate_score(score):
    if 0 < score > 100 or score.isdigit() != True:
        print("Pro favor ingrese una notra valida entre 0 y 100")
        score = input("Student's correct score: ")
    return score

add_student()
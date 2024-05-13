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

def validate_score(score):
    if 0 < score > 100:
        print("Pro favor ingrese una notra valida entre 0 y 100")
        score = input("Student's correct score: ")
    return score


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
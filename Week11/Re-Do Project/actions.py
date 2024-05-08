students = []

def add_student():
    try:
        student = {}
        student["name"]=input("Student's full name: ")
        student["group"]=input("Student's group number: ")
        student["spanish_score"]=input("Student's spanish score: ")
        student["english_score"]=input("Student's english score: ")
        student["scienses_score"]=input("Student's sciences score: ")
        student["social_studies_score"]=input("Student's social studies score: ")
        student["score_avg"]= (int(student["spanish_score"])+int(student["english_score"])+int(student["social_studies_score"])+int(student["scienses_score"])) /4
        print("")
        print("Student successfully added!!")
        students.append(student)
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')


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
students = []

def add_student():
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


def show_all_students():
    print(students)


def calculate_score_avg():
    print("")
students = [{'name': 'Jorge', 
            'group': '10-3',
            'spanish_score': '90',
            'english_score': '80',
            'scienses_score': '70',
            'social_studies_score': '96',
            'score_avg': 84.0},
            {'name': 'Juan', 
            'group': '10-2',
            'spanish_score': '90',
            'english_score': '80',
            'scienses_score': '90',
            'social_studies_score': '96',
            'score_avg': 89.0},
            {'name': 'Ana', 
            'group': '11-2',
            'spanish_score': '90',
            'english_score': '90',
            'scienses_score': '90',
            'social_studies_score': '90',
            'score_avg': 90.0},
            {'name': 'Lucas', 
            'group': '10-2',
            'spanish_score': '70',
            'english_score': '70',
            'scienses_score': '70',
            'social_studies_score': '70',
            'score_avg': 70.0}
            ]

#sorted_students = sorted(students, key=lambda x: x['score_avg'], reverse=True)

#print(sorted_students[:3])

all_students_avg = 0

for student in students:
   all_students_avg += student["score_avg"]
print(all_students_avg / len(students))
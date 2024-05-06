import actions
import data


def menu(user_option):
        while True:
            try:

                print(' ')
                print('Escoja la operacion a realizar:')
                print(' ')
                print('1. Add Student')
                print('2. Show all Students')
                print('3. Top 3 Students')
                print('4. Average grade of all students')
                print('5. Export Students to CSV')
                print('6. Import from CSV.')
                print('7. Exit.')
                print(' ')
                user_option = int(input('Select the user option you want to perform: ' ))
                print(' ')

                if user_option == 1:
                    print("Adding a student...")
                    actions.add_student()
                elif user_option == 2:
                    print("Showing all students...")
                    actions.show_all_students()
                elif user_option == 3:
                    actions.show_top_score_avg()
                elif user_option == 4:
                    actions.show_general_avg_score()
                elif user_option == 5:
                    data.export_students_csv("students.csv",actions.students)
                elif user_option == 6:
                    data.import_students("students.csv")
                elif user_option == 7:
                    break
                else:
                    print("Invalid option. Please try again.")
                
            except ValueError as error:
                print("Type a valid numeric value option from the menu.")
                print(f"Error info.{error}")
            
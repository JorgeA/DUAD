from datetime import date

class User:
    date_of_birth = {}
    
    def __init__(self, year, month, day):
        self.date_of_birth = {'year': year, 'month': month, 'day': day}

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth['year']
        if (today.month, today.day) < (self.date_of_birth['month'], self.date_of_birth['day']):
            age -= 1
        return age


def my_function(my_user):
    print("El ingreso al sistema es solo autolizado para mayores de edad")
    if my_user.age >= 18:
        print("Bienvenido al sistema")
    else:
        print("Lo siento, usted es menor de edad")

my_user = User(1990, 1, 1)
my_function(my_user)
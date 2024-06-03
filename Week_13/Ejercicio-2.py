#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números,
# y arroje una excepción de no ser así.

def check_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise Exception("Error: Todos los parametros deben ser numeros")
        return func(*args)
    return wrapper

@check_numbers
def my_function(a, b):
    print(a + b)

my_function(1, 3)
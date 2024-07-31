#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Parametros de la funcion: {args},{kwargs}")
        result = func(*args, **kwargs)
        print(f"Resultado de la funcion: {result}")
        return result
    return wrapper

@decorator
def my_function(a, b):
    return a + b 

my_function(5, 6)
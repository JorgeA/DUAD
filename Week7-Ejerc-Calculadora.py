def addition(current_num, num):
    try:
        result = current_num + num
        print(f'El resultado de sumar: {current_num} + {num} = {result}')
        return result
    except ValueError as error:
        print(f'Por favor ingresa un numero valido. {error}')


def subtract(current_num, num):
    result = current_num - num
    print(f'El resultado de restar: {current_num} - {num} = {result}')
    return result


def multiply(current_num, num):
    result = current_num * num
    print(f'El resultado de multiplicar: {current_num} * {num} = {result}')
    return result


def divide(current_num, num):
    try:
        result = current_num / num
        print(f'El resultado de dividir: {current_num} / {num} = {result}')
        return result
    except ZeroDivisionError as error:
        print(f'Hubo un error en la division ya que no se puede dividir por cero: {error}')


def reset_current_num():
    return 0


def menu(current_num):
    while True:
        try:
            print(' ')
            print('Escoja la operacion a realizar:')
            print(' ')
            print('1. Suma')
            print('2. Resta')
            print('3. Multiplicacion')
            print('4. Division')
            print('5. Borrar Numero Actual')
            print('6. Salir de Calculadora.')
            print(' ')
            option = int(input('Ingrese el numero de la operacion a realizar: ' ))
            print(' ')
            if option == 1:
                current_num = addition(current_num, int(input('Ingrese el segundo numero : ')))
            elif option == 2:
                current_num = subtract(current_num, int(input('Ingrese el segundo numero : ')))
            elif option == 3:
                current_num =  multiply(current_num, int(input('Ingrese el segundo numero : ')))
            elif option == 4:
                current_num =  divide(current_num, int(input('Ingrese el segundo numero : ')))
            elif option == 5:
                current_num = int(input('Ingrese el nuevo numero : '))
            elif option == 6:
                break
        except ValueError as e:
            print(f'Ingrese un valor numerico: {e}')

initial_num = int(input('Ingrese un número inicial: '))
menu(initial_num)
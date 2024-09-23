contador = 0
lista = []
num_mayor = 0 

while (contador < 10):
    number = int(input("Ingresa un numero: "))
    lista.append(number)
    contador +=1

for item in lista:
    if item > num_mayor:
        num_mayor = item
print(lista)
print(f"El numero mayor que ingresaste fue: {num_mayor}")
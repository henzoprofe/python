numero = int(input("Ingrese un número para verificar si es primo\nNúmero:"))
contador = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1
if contador == 2:
    print("El número ingresado es primo")
else:
    print("El número ingresado no es primo")

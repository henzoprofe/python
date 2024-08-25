print("Este programa encuentra los primos entre 1 y el tope ingresado")
tope = int(input("Ingrese el tope\nTope:"))
cuantos = 0
for numero in range(1, tope + 1):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    if contador == 2:
        cuantos += 1
        print(f"El número {numero} es primo")
#    else:
#        print(f"El número {numero} no es primo")
print(f"En total hay {cuantos} primos entre 1 y {tope}")

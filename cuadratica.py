print("Programa para resolver cuadraticas")
opcion = 2
while True:
    while True:
        a = float(input("Ingrese el coeficiente cuadrático:"))
        if a != 0:
            break
        else:
            print("El coeficiente cuadrático no puede ser cero")
    b = float(input("Ingrese el coeficiente lineal:"))
    c = float(input("Ingrese el coeficiente libre:"))
    disc = b * b - 4 * a * c
    print("El discriminante es:", disc)
    if disc < 0:
        print("No existe solución real\nExisten dos soluciones conplejas")
        xc1 =(-b - (-disc)**0.5) / (2 * a)
        xc2 =(-b + (-disc)**0.5) / (2 * a)
        print("Las soluciones son",xc1," y ",xc2)
    elif disc == 0:
        print("Existe única solución real, x=", (-b / (2 * a)))
    else:
        print("Existen dos soluciones reales:\nx1=", (-b - disc**0.5) / (2 * a)," y x2=",(-b + disc**0.5) / (2 * a),
        )
    opcion = float(input("Presione 1 para salir\tPresione 2 para resolver otra ecuación\nOpcion:"))
    if opcion == 1:
        break
print("Gracias por usar el programa")

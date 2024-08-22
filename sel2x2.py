print("Ordene las ecuaciones y luego ingrese los coeficientes de forma ordenada")
a1 = float(input("a1="))
b1 = float(input("b1="))
c1 = float(input("c1="))
a2 = float(input("a2="))
b2 = float(input("b2="))
c2 = float(input("c2="))

d = a1*b2-a2*b1
if d == 0.0:
    dp = a1*c2-a2*c1
    if dp == 0.0:
        print("Existen infinitas soluciones")
        print("Las soluciones tienen la forma:")
        print("y=({:.2f}-{:.2f}x)/{:.2f}".format(c1, b1, a1))
    else:
        print("No existe solución")
else:
    x = (b2*c1-b1*c2)/(a1*b2-a2*b1)
    y = (a1*c2-a2*c1)/(a1*b2-a2*b1)
    print("La solución es:\nx={:.2f}\ty={:.2f}".format(x, y))
printf("Gracias por usar HAMSoftware")

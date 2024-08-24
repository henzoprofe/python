a=float(input("Ingrese el valor del coeficiente cuadrático: "))
b=float(input("Ingrese el valor del coeficiente lineal: "))
c=float(input("Ingrese el valor del coeficiente libre: "))
discriminante=(b**2-4*a*c)
if discriminante==0:
  print("Existe única solución real")
elif discriminante<0:
  print("No existe solución real")
else:
  print("Existen dos soluciones reales")

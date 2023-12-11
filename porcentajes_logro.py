ins = float(input("Ingrese insuficientes: "))
suf = float(input("Ingrese suficientes: "))
bueno = float(input("Ingrese buenos: "))
mbueno = float(input("Ingrese muy buenos: "))

total = ins + suf + bueno + mbueno

pins = round((100 * ins / total),1)
psuf = round((100 * suf / total),1)
pbueno = round((100 * bueno / total),1)
pmbueno = round((100 * mbueno / total),1)

print(f"El total de alumnos es {total}")
print(f"I={pins}%\nS={psuf}%\nB={pbueno}\nMB={pmbueno}")
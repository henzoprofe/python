import tkinter as tk
from math import sqrt

# Crear la ventana principal
root = tk.Tk()
root.title("Resolver Ecuación Cuadrática")

# Etiquetas y campos de entrada para a, b, c
label_a = tk.Label(root, text="a:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=2)

label_b = tk.Label(root, text="b:")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=2)

label_c = tk.Label(root, text="c:")
label_c.grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=2)

# Área para mostrar los resultados
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Botón para resolver
solve_button = tk.Button(root, text="Resolver")
solve_button.grid(row=3, column=3, columnspan=2)

# Lógica para resolver la ecuación cuadrática usando lambda
solve_button.config(command=lambda: (
    # Bloque try-except dentro de lambda
    (lambda: (
        (lambda a, b, c, discriminante: (
            result_label.config(text=f"Discriminante: {discriminante}\nDos soluciones: {(-b + sqrt(discriminante)) / (2*a):.2f} y {(-b - sqrt(discriminante)) / (2*a):.2f}")
        ) if discriminante > 0 else (
            result_label.config(text=f"Discriminante: {discriminante}\nUna solución: {-b / (2*a):.2f}")
        ) if discriminante == 0 else (
            result_label.config(text=f"Discriminante: {discriminante}\nNo hay soluciones reales")
        ))(
            float(entry_a.get()), 
            float(entry_b.get()), 
            float(entry_c.get()), 
            float(entry_b.get())**2 - 4*float(entry_a.get())*float(entry_c.get())
        )
    ))()
) if all(map(lambda x: x.replace('.', '', 1).isdigit(), [entry_a.get(), entry_b.get(), entry_c.get()])) else (
    result_label.config(text="Introduce valores numéricos válidos")
))

# Iniciar la aplicación
root.mainloop()

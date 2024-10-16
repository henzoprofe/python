import tkinter as tk
from tkinter import messagebox

# Función para realizar la suma
def sumar():
    try:
        # Obtener el valor ingresado por el usuario y convertirlo a número
        numero = int(entry_numero.get())
        resultado = numero + 34
        # Mostrar el resultado en un mensaje emergente
        messagebox.showinfo("Resultado", f"El resultado es: {resultado}")
    except ValueError:
        # En caso de error en la conversión, mostrar un mensaje de error
        messagebox.showerror("Error", "Por favor ingresa un número válido")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Suma con 34")

# Etiqueta y campo de entrada para el número
label_numero = tk.Label(ventana, text="Ingresa un número:")
label_numero.pack()

entry_numero = tk.Entry(ventana)
entry_numero.pack()

# Botón para realizar la suma
boton_sumar = tk.Button(ventana, text="Sumar 34", command=sumar)
boton_sumar.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

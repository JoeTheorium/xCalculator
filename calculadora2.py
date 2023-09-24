import tkinter as tk
from tkinter import messagebox
import math
import sympy

# Función para actualizar el visor con el número clickeado
def agregar_numero(numero):
    visor.insert(tk.END, numero)

# Función para realizar cálculos y mostrar el resultado en el visor
def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Error")

# Función para explicar la operación en un modal
def explicar():
    try:
        operacion = visor.get()
        explicacion = f"La operación {operacion} se realiza de la siguiente manera:\n"
        
        # Utilizamos sympy para simplificar y explicar la operación
        operacion_simplificada = sympy.sympify(operacion)
        explicacion += str(operacion_simplificada)
        
        messagebox.showinfo("Explicación", explicacion)
    except Exception as e:
        messagebox.showerror("Error", "No se puede explicar esta operación")

# Función para calcular el porcentaje
def porcentaje():
    try:
        expresion = visor.get()
        resultado = eval(expresion) / 100
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Error")

# Función para calcular la raíz cuadrada
def raiz_cuadrada():
    try:
        expresion = visor.get()
        resultado = math.sqrt(float(eval(expresion)))
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Error")

# Función para borrar el último dígito
def borrar_ultimo():
    expresion = visor.get()
    nueva_expresion = expresion[:-1]
    visor.delete(0, tk.END)
    visor.insert(tk.END, nueva_expresion)

# Función para calcular la potencia
def potencia():
    try:
        expresion = visor.get()
        resultado = eval(expresion) ** 2
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Error")

# Función para calcular el logaritmo
def logaritmo():
    try:
        expresion = visor.get()
        resultado = math.log(float(eval(expresion)))
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Error")

# Función para calcular el logaritmo natural
def logaritmo_natural():
    try:
        expresion = visor.get()
        resultado = math.log(float(eval(expresion)), math.e)
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except Exception as e:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear el visor
visor = tk.Entry(ventana, font=('Arial', 24), justify='right', bd=10)
visor.grid(row=0, column=0, columnspan=4)

# Definir los botones en un diseño más estándar
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '⌫', '√', '%', '^', 'log', 'ln'
]

# Función para agregar operadores y números al visor
row, col = 1, 0
for boton in botones:
    if boton == '=':
        tk.Button(ventana, text=boton, padx=20, pady=20,
                  font=('Arial', 20),
                  command=calcular).grid(row=row, column=col)
    elif boton == '⌫':
        tk.Button(ventana, text=boton, padx=20, pady=20,
                  font=('Arial', 20),
                  command=borrar_ultimo).grid(row=row, column=col)
    elif boton == '√':
        tk.Button(ventana, text=boton, padx=20, pady=20,
                  font=('Arial', 20),
                  command=raiz_cuadrada).grid(row=row, column=col)
    elif boton == '%':
        tk.Button(ventana, text=boton, padx=20, pady=20,
                  font=('Arial', 20),
                  command=porcentaje).grid(row=row, column=col)
    elif boton == '^':
        tk.Button(ventana, text=boton, padx=20, pady=20,
                  font=('Arial', 20),
                  command=potencia).grid(row=row, column=col)
    elif boton == 'log':
        tk.Button(ventana, text=boton, padx=20, pady=20,
                  font=('Arial', 20),
                  command=logaritmo).grid(row=row, column=col)
    elif boton == 'ln':
        tk.Button(ventana, text=boton, padx=20, pady=20,
                  font=('Arial', 20),
                  command=logaritmo_natural).grid(row=row, column=col)
    else:
        tk.Button(ventana, text=boton, padx=20, pady=20,
                  font=('Arial', 20),
                  command=lambda boton=boton: agregar_numero(boton)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Botón de explicar
tk.Button(ventana, text="Explicar", padx=20, pady=20,
          font=('Arial', 20),
          command=explicar).grid(row=row, column=col, columnspan=2)

# Botón de borrar todo
tk.Button(ventana, text="C", padx=20, pady=20,
          font=('Arial', 20),
          command=lambda: visor.delete(0, tk.END)).grid(row=row, column=col+2)

# Iniciar el bucle principal
ventana.mainloop()

import tkinter as tk
import math
# Las funciones para realizar operaciones científicas son las siguientes
def calcular():
    try:
        expresion = pantalla.get("1.0", tk.END)
        resultado = eval(expresion)
        actualizar_pantalla(resultado)
    except Exception as e:
        actualizar_pantalla("Error")

def actualizar_pantalla(valor):
    pantalla.config(state=tk.NORMAL)
    pantalla.delete(1.0, tk.END)
    pantalla.insert(tk.END, valor)
    pantalla.config(state=tk.DISABLED)

def borrar():
    pantalla.config(state=tk.NORMAL)
    pantalla.delete(1.0, tk.END)
    pantalla.config(state=tk.DISABLED)

def calcular_raiz_cuadrada():
    try:
        valor = float(pantalla.get("1.0", tk.END))
        resultado = math.sqrt(valor)
        actualizar_pantalla(resultado)
    except Exception as e:
        actualizar_pantalla("Error")

# Esta es la configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora Científica")
ventana.geometry("500x600")
ventana.configure(bg="black")

# El título de la calculadora
titulo = tk.Label(ventana, text="Mega Calculadora", bg="black", fg="white", font=("Arial", 20))
titulo.pack(pady=10)

# Creación de la pantalla
pantalla = tk.Text(ventana, height=2, width=16, state=tk.DISABLED, bg="black", fg="white", font=("Arial", 24))
pantalla.pack(pady=10)

# Creación del contenedor para los botones con el gestor de geometría pack
contenedor_botones = tk.Frame(ventana, bg="black")
contenedor_botones.pack()

# Definición de los botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'ok'
]

# Creación y colocación de los botones en el contenedor respectivo
row_val = 0
col_val = 0

for boton_texto in botones:
    if boton_texto == 'C':
        tk.Button(contenedor_botones, text=boton_texto, padx=20, pady=20, command=borrar, bg="red", fg="white", font=("Arial", 16)).grid(row=row_val, column=col_val)
    elif boton_texto == '√':
        tk.Button(contenedor_botones, text=boton_texto, padx=20, pady=20, command=calcular_raiz_cuadrada, bg="red", fg="white", font=("Arial", 16)).grid(row=row_val, column=col_val)
    elif boton_texto == '=':
        tk.Button(contenedor_botones, text=boton_texto, padx=20, pady=20, command=calcular, bg="red", fg="white", font=("Arial", 16)).grid(row=row_val, column=col_val)
    else:
        tk.Button(contenedor_botones, text=boton_texto, padx=20, pady=20, command=lambda t=boton_texto: pantalla.insert(tk.END, t), bg="red", fg="white", font=("Arial", 16)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

ventana.mainloop()

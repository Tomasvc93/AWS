import tkinter as tk

# Esta es la función para dibujar una cara triste de un sol
def dibujar_sol_triste():
    # Dibujo del sol
    canvas.create_oval(100, 100, 300, 300, fill='yellow', outline='yellow', width=2)
    
    
# Dibujo de la cara triste
    canvas.create_oval(150, 150, 250, 250, fill='white', outline='black', width=2)  # Cara
    canvas.create_arc(170, 190, 230, 220, start=0, extent=180, style=tk.ARC, outline='black', width=2)  # Cara triste
    canvas.create_oval(185, 175, 195, 185, fill='black')  # Ojo izquierdo
    canvas.create_oval(205, 175, 215, 185, fill='black')  # Ojo derecho

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Cara Triste de un Sol de Felipe")

# Creación de la pantalla o lienzo con canvas
canvas = tk.Canvas(ventana, width=400, height=400, bg='white')
canvas.pack()

# Botón para dibujar la cara triste del sol
boton_dibujar = tk.Button(ventana, text="Dibujar Cara Triste", command=dibujar_sol_triste)
boton_dibujar.pack()

ventana.mainloop()

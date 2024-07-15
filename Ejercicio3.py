# Dibujar rombo centrado a partir de ingresar un número
# Ejemplo Rombo de 5 filas
# *
# **
# ***
# **
# *
             
def rombo():

    while True:
        numero = input("ingrese un número impar para dibujar un rombo:")
        numero = int(numero)

        if numero % 2 == 1:
            break
        print("el número ingresado debe ser impar")
    
    mitad_fila = numero // 2
    numero = numero + 1

    for fila in range(numero):
        if fila <= mitad_fila + 1:
            print("*" * fila, end="")
            print()
        else:
            print("*" * mitad_fila, end="")
            mitad_fila = mitad_fila - 1
            print()

rombo()



    



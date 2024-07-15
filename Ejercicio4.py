# Crear función donde elegir entre suma, resta, multiplicación, división y efectuar cálculo de dos valores ingresados.

def calcular(operacion, numero1, numero2):
    if operacion == "suma":
        return numero1 + numero2
    elif operacion == "resta":
        return numero1 - numero2
    elif operacion == "multiplicación":
        return numero1 * numero2
    elif operacion == "división":
        return numero1 / numero2
    else:
        raise ValueError("Operación no válida")


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

operacion = input("Ingrese la operación a realizar (suma, resta, multiplicación, división): ")

resultado = calcular(operacion, numero1, numero2)

resultado = str(resultado)

print("El resultado es: " + resultado)

calcular(operacion, numero1, numero2)
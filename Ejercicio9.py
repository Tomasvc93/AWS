def calcular_imc():
    peso = float(input("Ingresa tu peso en Kgs: "))
    altura = float(input("Ingresa tu altura en cms: "))
    altura_metros = altura / 100
    imc = peso / (altura_metros ** 2)
    imc = str(imc)
    print("Tu IMC es: " + imc)
    imc = float(imc)

    if imc <= 18.5:
        print("tu nivel de peso es bajo")
    elif imc <= 24.9:
        print("tu nivel de peso es normal")
    elif imc <= 29.9:
        print("tu nivel de peso es de sobrepeso")
    else:
        print("tu nivel de peso es de obesidad")
    
calcular_imc()




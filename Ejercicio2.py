# Al ejecutar una función, se pide ingresar una frase cualquiera y debe dar como resultado el conteo de caracteres.

def conteo_caracteres():
    frase = input("ingresar frase: ")
    numero_caracteres = len(frase)

    print("el número de caracteres de la frase es:")
    print(numero_caracteres)

conteo_caracteres()



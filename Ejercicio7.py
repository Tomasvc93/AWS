# Ingresar una cadena con números de la siguiente manera “ 23 34 1 45 67 78 100 “ y lo ordene, depende de ustedes separarlos por espacio, guión, etc.

cadena_numeros = "23 34 1 45 67 78 100"
lista_numeros = [int(lista_numero) for lista_numero in cadena_numeros.split()]
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)
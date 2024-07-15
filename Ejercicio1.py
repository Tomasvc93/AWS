# Mediante una función pedir tu nombre, apellido y edad (algún dato extra si lo desean) e imprimir los datos en pantalla.

def data_input():
    name = input("ingrese su nombre: ")
    surname = input("ingrese su apellido: ")
    age = input("ingrse su edad: ")
    birth_date = input("ingrese su fecha de nacimiento: ")
    fav_colour = input("ingrese su color favorito: ")
    fav_food = input("ingrese su comida favorita: ")
    football_team = input("ingrese su equipo de football favorito: ")

    print("tu nombre es: " + name)
    print("tu apellido es: " + surname)
    print("tu edad es: " + age)
    print("tu fecha de nacimiento es: " + birth_date)
    print("tu color favorito es: " + fav_colour) 
    print("tu comida favorita es: " + fav_food)
    print("tu equipo de football favorito es: " + football_team)

data_input()


# Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
# qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
# de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
# similar al siguiente:
# 1. Calcular el área de un círculo
# 2. Calcular el área de un triángulo
# 3. Calcular el área de un rectángulo
# 4. Salir
# Introduce una opción (1-4):
# El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la
# opción 4.
# Hay que diseñar y definir las siguientes funciones:

# • calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y
#   retorna su área.

# • calcular_area_triangulo: recibe como parámetros de entrada la base y la altura
#   del triángulo y retorna su área.

# • calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura
#   del rectángulo y retorna su área.

# • mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.

# • main(): lee por teclado la opción seleccionada por el usuario, valida que la opción
#   está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función
#   correspondiente en función de la opción seleccionada.

# • opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre
#   sea mayor que 0 y una vez que ha validado el radio llamará a la función
#   calcular_area_circulo.

# • opcion2: descripción: lee por teclado el valor de la base y la altura del triángulo,
#   valida que los dos datos son mayores que 0 y una vez que los ha validado llamará
#   a la función calcular_area_triangulo.

# • opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que
#   los dos datos son mayores que 0 y una vez que los ha validado llamará a la función
#   calcular_area_rectangulo.

import math #importa "math" para representar PI

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def mostrar_menu():
    print("\n<<<<<<<<<<< MENÚ >>>>>>>>>>>>>")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

def opcion1():
    radio = float(input("Introduce el radio del círculo: "))
    if radio > 0:
        area = calcular_area_circulo(radio)
        print("El área del círculo es: "+str(area))
    else:
        print("El radio debe ser mayor que 0")

def opcion2():
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_triangulo(base, altura)
        print("El área del triángulo es: "+str(area))
    else:
        print("La base y la altura deben ser mayores que 0")

def opcion3():
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_rectangulo(base, altura)
        print("El área del rectángulo es: "+str(area))
    else:
        print("La base y la altura deben ser mayores que 0")

def main(n):
    while n < 1 or n > 4:
        n = int (input("Introduce una opción a realizar: "))
        if n < 1 or n > 4:
            print("Selecciona una opción vádila >:(")
        else:
            match n:
                case 1:
                    opcion1()
                    
                case 2:
                    opcion2()
                
                case 3:
                    opcion3()
                    
                case 4:
                    print("Saliste del Programa")
    return n

n = 0    
while n != 4:
    mostrar_menu()
    n = main(n)
    





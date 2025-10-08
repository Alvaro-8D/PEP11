# Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
# valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
# que muestre un aviso y vuelva a pedir el valor.


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














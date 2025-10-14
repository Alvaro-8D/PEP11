# Crea un paquete llamado matemáticas que contenga tres módulos:
# • operaciones: creado en la práctica anterior.
# • figuras: tendrá las siguientes funciones.
#   ◦ area_rectangulo(base, altura): devuelve el área.
#   ◦ area_triangulo(base, altura): devuelve el área.
#   ◦ area_circulo(radio): devuelve el área.
# • conversiones.py: tendrá las siguientes funciones
#   ◦ a_binario(n): devuelve la representación binaria de un número entero en forma de cadena.
#   ◦ a_hexadecimal(n): devuelve la representación hexadecimal de un número entero en forma de cadena.
#   ◦ a_entero(texto): convierte una cadena numérica en un entero (controlando errores si el texto no es válido)
# Recuerda que debes incluir el fichero __init__.py aunque esté vacío.
# Crea un programa principal main.py que muestre un menú que permita elegir entre:
# • Operaciones matemáticas
# • Cálculo de áreas geométricas
# Según la opción elegida, pida al usuario los datos necesarios y muestre el resultado correspondiente.
# El programa principal (main.py) debe seguir la estructura:
# # imports de la librería estándar
# # imports de librerías de terceros
# # imports de módulos propios
# # Definición de funciones principales
# def main():
#     """Función principal del programa"""
#     print("Hola, este es el programa principal")
# # Bloque para asegurar ejecución sólo si el archivo es el principal
# if __name__ == "__main__":
#     # Se pueden procesar argumentos, inicializar variables, etc.
#     main()

import math
from matematicas import operaciones, figuras, conversiones

def menu():
    """Muestra el menú principal."""
    print("\nMenú principal")
    print("1. Operaciones matemáticas básicas")
    print("2. Cálculo de áreas geométricas")
    print("3. Conversiones numéricas")
    print("4. Salir")

def main():
    """Función principal del programa"""
    while True:
        menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))

            print(f"Suma: {operaciones.suma(a, b)}")
            print(f"Resta: {operaciones.resta(a, b)}")
            print(f"Multiplicación: {operaciones.multiplicacion(a, b)}")
            print(f"División: {operaciones.division(a, b)}")

        elif opcion == "2":
            print("\nCálculo de áreas:")
            print("1. Rectángulo")
            print("2. Triángulo")
            print("3. Círculo")
            figura = input("Elige una figura (1-3): ")

            if figura == "1":
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("Área del rectángulo:", figuras.area_rectangulo(base, altura))
            elif figura == "2":
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("Área del triángulo:", figuras.area_triangulo(base, altura))
            elif figura == "3":
                radio = float(input("Radio: "))
                print("Área del círculo:", figuras.area_circulo(radio))
            else:
                print("Opción no válida.")

        elif opcion == "3":
            print("\nConversiones numéricas:")
            n = input("Introduce un número: ")
            print("Binario:", conversiones.a_binario(n))
            print("Hexadecimal:", conversiones.a_hexadecimal(n))
            print("Convertir de texto a entero:", conversiones.a_entero(n))

        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()







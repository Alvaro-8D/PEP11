# Investiga usos habituales del fichero __init__.py de un paquete y usa el ejemplo anterior
# para configurar y probar alguno de ellos.

import matematicas

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

            print(f"Suma: {matematicas.suma(a, b)}")
            print(f"Resta: {matematicas.resta(a, b)}")
            print(f"Multiplicación: {matematicas.multiplicacion(a, b)}")
            print(f"División: {matematicas.division(a, b)}")

        elif opcion == "2":
            print("\nCálculo de áreas:")
            print("1. Rectángulo")
            print("2. Triángulo")
            print("3. Círculo")
            figura = input("Elige una figura (1-3): ")

            if figura == "1":
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("Área del rectángulo:", matematicas.area_rectangulo(base, altura))
            elif figura == "2":
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("Área del triángulo:", matematicas.area_triangulo(base, altura))
            elif figura == "3":
                radio = float(input("Radio: "))
                print("Área del círculo:", matematicas.area_circulo(radio))
            else:
                print("Opción no válida.")

        elif opcion == "3":
            print("\nConversiones numéricas:")
            n = input("Introduce un número: ")
            print("Binario:", matematicas.a_binario(n))
            print("Hexadecimal:", matematicas.a_hexadecimal(n))
            print("Convertir de texto a entero:", matematicas.a_entero(n))

        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()







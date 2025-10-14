# Modifica el programa principal (main.py) del ejercicio anterior para que siga la siguiente
# estructura:
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


import operaciones as op

def main(): # Función principal del programa
    print("Hola, este es el programa principal")
    print("Dame dos números: ")
    a = int (input("Primer Número: "))
    b = int (input("Segundo Número: "))

    print(f"Suma: {op.suma(a, b)}")
    print(f"Resta: {op.resta(a, b)}")
    print(f"Multiplicación: {op.multiplicacion(a, b)}")
    print(f"División: {op.division(a, b)}")
    
if __name__ == "__main__": # Bloque para asegurar ejecución sólo si el archivo es el principal
    main()

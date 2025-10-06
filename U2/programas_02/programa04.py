# Escribe un programa que use un bucle while y le pida continuamente al usuario que
# introduzca un número hasta que ingrese 45 como la número de salida secreto, en cuyo
# caso el mensaje "¡Has dejado el bucle con éxito" debe imprimirse en la pantalla y el bucle
# debe terminar.
# Haz dos versiones del programa:
# • Versión 1: Utiliza el concepto de ejecución condicional y la instrucción break.
# • Versión 2: Sin usar break, el bucle while controla la condición de salida.

print("OPCIÓN 1 (con BREAK)")
i = -1
while i == i:
    i = int (input("Dime el número secreto: "))
    if i == 45:
        print("¡Enhorabuena pequeño saltamontes, has dejado el bucle con éxito!")
        break

print("\nOPCIÓN 2 (SIN BREAK)")
i = -1
while i != 45:
    i = int (input("Dime el número secreto: "))
    if i == 45:
        print("¡Enhorabuena pequeño saltamontes, has dejado el bucle con éxito!")
    
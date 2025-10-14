# programa02
# Modifica el programa anterior para que solo se importen las funciones del módulo math
# que se usan en el programa.

from math import sin, cos, sqrt, pow, radians

print("Seleccione la operación que desea realizar:")
print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números")

opcion = input("Introduce una opción (1-4): ")

if opcion == "1":
    angulo = float(input("Introduce el ángulo en grados: "))
    print(f"El seno de {angulo}° es: {sin(radians(angulo))}")
elif opcion == "2":
    angulo = float(input("Introduce el ángulo en grados: "))
    print(f"El coseno de {angulo}° es: {cos(radians(angulo))}")
elif opcion == "3":
    numero = float(input("Introduce un número: "))
    if numero < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        print(f"La raíz cuadrada de {numero} es: {sqrt(numero)}")
elif opcion == "4":
    base = float(input("Introduce la base: "))
    exponente = float(input("Introduce el exponente: "))
    print(f"{base} elevado a {exponente} es: {pow(base, exponente)}")
else:
    print("Opción no válida.")

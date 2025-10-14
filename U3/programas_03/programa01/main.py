# programa01
# Crea un módulo llamado op que contenga cuatro funciones básicas
# relacionadas con op numéricas:
# • suma(a, b) → devuelve la suma de dos números.
# • resta(a, b) → devuelve la resta de dos números.
# • multiplicacion(a, b) → devuelve la multiplicación de dos números.
# • division(a, b) → devuelve la división de dos números (controlando la división entre cero).
# Crea un programa principal main.py que importe el módulo op, pida al usuario
# dos números y muestre los resultados de aplicar cada una de las funciones anteriores.

import operaciones as op

def main():
    print("Dame dos números: ")
    a = int (input("Primer Número: "))
    b = int (input("Segundo Número: "))

    print(f"Suma: {op.suma(a, b)}")
    print(f"Resta: {op.resta(a, b)}")
    print(f"Multiplicación: {op.multiplicacion(a, b)}")
    print(f"División: {op.division(a, b)}")

main()
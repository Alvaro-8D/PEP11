# Escribe un programa que pida primero un número par y luego un número impar (positivos
# o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
# impar respectivamente), se mostrará un aviso.

par = int (input("Dime un número PAR: "))
if (par % 2) != 0:
    print("Esto no es un número par")


impar = int (input("Dime un número IMPAR: "))
if (impar % 2) == 0:
    print("Esto no es un número impar")

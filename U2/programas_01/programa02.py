# Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
# es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
# negativo) y si el valor no es correcto, mostrará un aviso.

par = int (input("Dime un número PAR: "))
if (par % 2) != 0:
    print("Esto no es un número par")
else:
    impar = int (input("Dime un número IMPAR: "))
    if (impar % 2) == 0:
        print("Esto no es un número impar")



# Escribe un programa que pida un número y muestre una lista de números desde 1 al
# número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
# pedirá que se introduzca de nuevo, hasta que sea correcto.

i = -1
while i > 10 or i < 1:
    i = int (input("Dime un númerod el 1 al 10: "))
for i in range(1,(i+1)):
    print(i, end="\n")




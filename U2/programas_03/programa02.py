# Escribe un programa que pida un número y muestre una lista de números desde 1 al
# número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
# pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto.
# Controla las posibles excepciones a la hora de introducir el número por teclado.


ok = True
while ok:
    try:
        i = -1
        while i > 10 or i < 1:
            i = int (input("Dime un númerod el 1 al 10: "))
        for i in range(1,(i+1)):
            print(i, end="\n")
        ok = False
    except Exception:
        print('Solo puedes introducir numeros enteros')
        ok = True








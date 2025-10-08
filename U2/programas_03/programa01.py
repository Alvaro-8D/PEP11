# Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
# pedir el número hasta que no se introduzca correctamente. Controla las posibles
# excepciones a la hora de introducir el número por teclado.

ok = True
while ok:
    try:
        i = -1
        while i > 10 or i < 1:
            i = int (input("Dime un númerod el 1 al 10: "))
        ok = False
        print("****** SALISTE DEL BUCLE **********")
    except Exception:
        print('Solo puedes introducir numeros enteros')
        ok = True






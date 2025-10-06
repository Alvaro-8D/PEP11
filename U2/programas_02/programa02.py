# Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
# pedir el número hasta que no se introduzca correctamente.
n = -1

while n < 1 or n > 10:
    n = int (input("Dime un numero del 1 al 10: "))
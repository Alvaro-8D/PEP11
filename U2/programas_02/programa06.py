# Escribe un programa que realice las siguientes operaciones:
# • Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
#   no se introduzca el número correcto.
# • Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
# • Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
#   desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
#   programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
#   indica que no quiere continuar el programa finaliza.

continuar = 3
while continuar == 3:    
    i = -1
    while i > 10 or i < 1:
        i = int (input("Dime un númerod el 1 al 10: "))
    j = 0
    for j in range(1,11):
        print(str(i)+" x "+str(j)+" = "+str(i*j), end="\n")
    continuar = 3
    while continuar != 1 and continuar != 2:
        continuar = int (input("Quieres continuar con otro número?\n si(1) / no(2)\n"))
    if continuar == 1:
        continuar = 3






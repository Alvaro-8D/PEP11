# Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
# suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
# la instrucción break y otra no.

print("OPCIÓN 1 (con BREAK)")
i = -1
suma = 0
contador = 0
while i == i:
    i = int(input("Dime el número 0 para acabar con esto: "))
    if i == 0:
        break
    else:
        suma += i
        contador += 1
print("\nSuma = " + str(suma) + " | Media = " + str(int (suma / contador)))

print("\nOPCIÓN 2 (SIN BREAK)")
i = -1
suma = 0
contador = 0
while i != 0:
    i = int(input("Dime el número 0 para acabar con esto: "))
    if i != 0:
        suma += i
        contador += 1
print("\nSuma = " + str(suma) + " | Media = " + str(int (suma / contador)))

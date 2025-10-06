# Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
# ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
# continue.

#Forma 1  <--------------------------------------<<<
print("\nUtilizo Bucle WHILE:")
i = 0
while i <= 10 and i >= 0:
    print(i, end=" ")
    i += 2

#Forma 2  <--------------------------------------<<<
print("\nUtilizo Bucle FOR:")
for i in range(0,11,2):
    print(i, end=" ")

#Forma 3  <--------------------------------------<<<
print("\nUtilizo Bucle WHILE y <Continue>:")
i = 0
while i <= 10 and i >= 0:
    i += 1

    if i%2 != 0:
        continue

    elif i%2 == 0:
        print(i, end=" ")
    

#Forma 4  <--------------------------------------<<<
print("\nUtilizo Bucle FOR y <Continue>:")
for i in range(0,11,2):

    if i%2 != 0:
        continue

    elif i%2 == 0:
        print(i, end=" ")









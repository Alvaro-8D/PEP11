# Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
# o que indique que son iguales.


a = int (input("Dime un numero: "))
b = int (input("Dime otro numero: "))

if a > b:
    print(str(a)+" es el numero mayor y "+str(b)+" es el numero menor")
else:
    if a == b:
        print("Ambos numeros son Iguales")
    else:
        print(str(b) + " es el numero mayor y "+str(a)+" es el numero menor") 
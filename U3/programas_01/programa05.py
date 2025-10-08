# Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
# en Python (globales, no locales y locales).

# --------------------------------------------------------------------------------------------------
print("Siempre hace referencia al Parámetro y no a la variable global")
def mostrar(x):
    x=2
    print(x)
x=10
mostrar(x)
# --------------------------------------------------------------------------------------------------
print("\nAl declarar la variable <Global>, se puede cambiar su valor desde la función")
def mostrar2():
    global a
    print(a)
    a = 2
a = 10
mostrar2() 
print(a,end=" Escribe 2 porque se cambió desde la funcion mostrar2()\n")
# --------------------------------------------------------------------------------------------------
print("\nAl declarar la variable <nonlocal>, se puede cambiar su valor desde\n la función padre pero no desde fuera de la función padre")
def mostrar3():
    def mostrar32():
        nonlocal a
        print(a)
        a = 3
    a = 2
    mostrar32()
    print(a,end=" La variable es visible y se puede cambiar desde dentro de ambas funciones\n")   
a = 10
mostrar3() 
print(a,end=" La variable es visible solo dentro dentro de mostrar3() y mostrar32()\n")
# --------------------------------------------------------------------------------------------------
print("\nSi quitamos <nonlocal>, YA NO se puede cambiar su valor desde\n la función padre")
def mostrar4():
    def mostrar42():
        a = 3
        print(a)
    a = 2
    mostrar42()
    print(a,end=" Solo se guardan los cambios de la variable hechos en la función padre\n")   
a = 10
mostrar4() 
print(a,end=" La variable es visible solo dentro dentro de mostrar4()\n")













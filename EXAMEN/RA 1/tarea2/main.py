a = int (input("Dime un numero entero: "))
b = float (input("Dime un numero decimal: "))
c = input("Dime un cadena: ")

print(str(a)+" es de tipo "+str(type(a)))
print(str(b)+" es de tipo "+str(type(b)))
print(str(c)+" es de tipo "+str(type(c)))

a2 = b2 = c2 = False

if(type(a) is int):
    a2 = True
if(type(b) is float):
    b2 = True
if(type(c) is str):
    c2 = True

if(a2 and b2 and c2):
    print(f"{a} + {b} = "+str(a+b))
else:
    print("ERROR: Alguno de los datos introducidos no es del tipo correcto")
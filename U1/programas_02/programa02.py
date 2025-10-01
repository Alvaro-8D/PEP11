# Escribe un programa que:
# - Cree una variable que almacene el número entero 6.
# - Muestre por pantalla el tipo del objeto que contiene el número 6.
# - Cree otra variable a la que se asigne la primera.
# - Compruebe con "is" si apuntan al mismo objeto.
# - Cambie el valor de la primera variable a "Hola".
# - Compruebe los tipos con isinstance().

var1 = 6
print(type(6), type(var1))

var2 = var1
print(type(6), type(var2))

print("¿Apuntan al mismo objeto?", var1 is var2)
print("¿No apuntan al mismo objeto?", var1 is not var2)

var1 = "Hola"
print(type("Hola"), type(var1))

print("¿var1 es int?", isinstance(var1, int))
print("¿var2 es int?", isinstance(var2, int))
print("¿var1 es str?", isinstance(var1, str))
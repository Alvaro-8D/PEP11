'''
Escribe un programa que use la función print() para
 Escribir un el número 34 en binario, otro en octal y otro en hexadecimal.
 Escribir los números 0b1001, 0o12, 0xa3f en decimal.
'''

print("Escribir un el número 34 en binario, otro en octal y otro en hexadecimal\n")
print(format(34,'b'))
print(format(35,'o'))
print(format(36,'x'))

print("\nEscribir los números 0b1001, 0o12, 0xa3f en decimal\n")
print(f"{0b1001}")
print(f"{0o12}")
print(f"{0xa3f}")
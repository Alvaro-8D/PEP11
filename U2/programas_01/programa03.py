# Escribe un programa que pida dos número y muestre su división. Se deben tener en
# cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.

num1 = int (input("Dime un número: "))
num2 = int (input("Dime otro número: "))

if num2 == 0:
    print("NO PUEDES DIVIDIR POR 0")
else:
    print(num1/num2)
from matematicas import *

def main():
    tabla_multiplicar(5)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    try:
        binario()
    except Exception:
        print("La Funcion BINARIO ha sido desabilitada para jugar Silksong")
    hexadecimal()
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    circulo()

if(__name__ == "__main__"):
    main()
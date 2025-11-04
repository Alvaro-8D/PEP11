def tabla_multiplicar(a):
    match a:
        case 7|8:
            print("No me sé la tabla del 7 ni del 8")
        case 0:
            print("¡¡¿¿Acaso se puede hacer la tabla del 0??!!")
        case _:
            for i in range(1,11):
                print(f"{a} x {i} = "+str(i*a))
    
    
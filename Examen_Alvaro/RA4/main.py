from funciones import *

def main():
    inventario = crear_inventario()

    agregar_producto(inventario,"P001","Portatil",[1000])
    agregar_producto(inventario,"P002","PC Gamer",[2000])

    # duplicado
    #agregar_producto(inventario,"P001","Portatil",[1000]) 
    print(inventario)

    actualizar_precio(inventario,"P001",1050)

    obtener_producto(inventario,"P002")

    analizar_precios_producto(inventario,"P001")


# ****** Programa Principal **********
if __name__ == "__main__":
    main()
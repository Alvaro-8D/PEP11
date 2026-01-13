def crear_inventario():
    inventario = {}
    return inventario

def agregar_producto(inventario,codigo,nombre,precio_inicial):
    if codigo in inventario:
        existe = False
    else:
        inventario[codigo] = (nombre, precio_inicial)
        existe = inventario

    return existe

def actualizar_precio(inventario,codigo,nuevo_precio):
    if codigo in inventario:
        inventario[codigo][1][len(inventario[codigo][1])] = nuevo_precio
        existe = inventario
    else:
        existe = False

    return existe

def obtener_producto(inventario,codigo):

    if codigo in inventario:
        existe = "PRODUCTO: "+str(inventario[codigo][0])+" | PRECIO ACTUAL: "+str(inventario[codigo][1][len(inventario[codigo][1])-1])
    else:
        existe = ""
    return existe

def analizar_precios_producto(inventario,codigo):
    if codigo in inventario:
        existe = sorted(inventario[codigo][1])
    else:
        existe = []
    return existe










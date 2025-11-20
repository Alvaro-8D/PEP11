# ============================================================
# :libro_azul: RESUMEN BASE PYTHON — VARIABLES, FUNCIONES, BUCLES Y MÓDULOS
# ============================================================
# =====================
# :pieza_de_puzle: VARIABLES Y TIPOS
# =====================
numero = 10
texto = "Hola Python"
decimal = 3.14
booleano = True
lista = [1, 2, 3, 4]
tupla = (5, 6)
diccionario = {"nombre": "Ana", "edad": 20}
print("Variable número:", numero)
print("Primer elemento de lista:", lista[0])
print("Diccionario:", diccionario["nombre"])
# =====================
# :caja_de_herramientas: FUNCIONES
# =====================
def saludar(nombre):
    print(f"Hola, {nombre}!")
def sumar(a, b):
    return a + b
def promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)
saludar("Carlos")
print("Suma:", sumar(3, 5))
print("Promedio:", promedio([10, 8, 9]))
# =====================
# :ciclón: BUCLES
# =====================
# for con range
for i in range(5):
    print("Número con range:", i)
# for con lista
colores = ["rojo", "verde", "azul"]
for color in colores:
    print("Color:", color)
# for con enumerate (índice y valor)
for indice, color in enumerate(colores):
    print(f"Índice {indice} -> {color}")
# for con diccionario
datos = {"nombre": "Luis", "edad": 22, "pais": "Chile"}
for clave, valor in datos.items():
    print(f"{clave}: {valor}")
# for con lista y condicional
numeros = [1, 2, 3, 4, 5, 6]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print("Números pares:", pares)
# while
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
# =====================
# :engranaje: MODULARIDAD (SIMULADA)
# =====================
# Supongamos que tenemos varios archivos:
#
# ├── __main__.py
# ├── operaciones.py
# ├── utilidades.py
#
# Ejemplo completo combinado aquí ↓
# === operaciones.py ===
def multiplicar(a, b):
    return a * b
def restar(a, b):
    return a - b
# === utilidades.py ===
def mostrar_lista(lista):
    for i, elemento in enumerate(lista):
        print(f"[{i}] {elemento}")
def es_par(numero):
    return numero % 2 == 0
# === __main__.py ===
def main():
    from math import sqrt
    # Uso de funciones importadas
    print("\n--- Ejemplo de __main__.py ---")
    print("5 x 3 =", multiplicar(5, 3))
    print("10 - 4 =", restar(10, 4))
    numeros = [2, 5, 8, 11, 14]
    mostrar_lista(numeros)
    pares = [n for n in numeros if es_par(n)]
    print("Solo pares:", pares)
    # Ejemplo con función del módulo math
    print("Raíz cuadrada de 16 =", sqrt(16))
    # Ejemplo con bucle dentro de main
    print("\nNúmeros mayores a 5:")
    for n in numeros:
        if n > 5:
            print(n)
# Llamada principal
if __name__ == "__main__":
    main()
# 3.1.5. Etapa 5: Diccionarios:
    #  Transforma tu colección en un diccionario donde:
    # ◦ La clave sea un identificador único ( título normalizado).
    # ◦ El valor sea otro diccionario con datos de la videojuego.
    # {
    #  "titulo": str,
    #  "anio": int,
    #  "genero": set
    # }
    #  Implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre el catálogo
    # usando la clave.
    #  Implementa funciones de búsqueda:
    # ◦ Exacta por título.
    # ◦ Parcial (contenga un fragmento en el título).
    # ◦ Por género o rango de años.
    #  Calcula estadísticas:
    # ◦ Número total de videojuegos.
    # ◦ Conteo por género.

















# PYTHON PROYECTO

from conjuntos import * # Lista de generos de los juegos
from tuplas import * # Lista de tuplas con los juegos

####################### FUNCIONES ############################
def crear_juego(catalogo):
    titulo = input("Título del nuevo juego: ")
    anio = int(input("Año: "))
    genero = input("Género(s) separados por '/': ")
    clave = titulo.lower().replace(" ", "_")
    if clave not in catalogo:
        catalogo[clave] = {
            "titulo": titulo,
            "anio": anio,
            "genero": set(genero.split("/"))
        }
        print("Juego añadido correctamente.")
    else:
        print("Ya existe un juego con ese nombre.")
#---------------------------------------------------------
def leer_juego(catalogo):
    nombre = input("Introduce el título exacto: ").lower().replace(" ", "_")
    if nombre in catalogo:
        print("Juego encontrado:", catalogo[nombre])
    else:
        print("No se encontró ese juego.")
#---------------------------------------------------------
def buscar_parcial(catalogo):
    fragmento = input("Escribe parte del nombre del juego: ").lower()
    encontrados = []
    for datos in catalogo.values():
        if fragmento in datos["titulo"].lower():
            encontrados.append(datos["titulo"])
    if encontrados:
        print("Coincidencias:", encontrados)
    else:
        print("No se encontraron juegos con ese fragmento.")
#---------------------------------------------------------
def buscar_por_genero(catalogo):
    buscar_genero = input("Género a buscar: ").lower()
    for datos in catalogo.values():
        for g in datos["genero"]:
            if buscar_genero == g.lower():
                print(datos["titulo"], "-", ", ".join(datos["genero"]))
#---------------------------------------------------------
def buscar_por_rango(catalogo):
    inicio = int(input("Año inicial: "))
    fin = int(input("Año final: "))
    for datos in catalogo.values():
        if inicio <= datos["anio"] <= fin:
            print(datos["titulo"], "-", datos["anio"])
#---------------------------------------------------------
def actualizar_juego(catalogo):
    clave = input("Título del juego a actualizar: ").lower().replace(" ", "_")
    if clave in catalogo:
        nuevo_anio = int(input("Nuevo año: "))
        catalogo[clave]["anio"] = nuevo_anio
        print("Juego actualizado:", catalogo[clave])
    else:
        print("No se encontró ese juego.")
#---------------------------------------------------------
def eliminar_juego(catalogo):
    clave = input("Título del juego a eliminar: ").lower().replace(" ", "_")
    if clave in catalogo:
        del catalogo[clave]
        print("Juego eliminado.")
    else:
        print("No se encontró ese juego.")
#---------------------------------------------------------
def estadisticas(catalogo):
    print("\n=== Estadísticas ===")
    print("Número total de juegos:", len(catalogo))
    conteo_generos = {}
    for datos in catalogo.values():
        for g in datos["genero"]:
            if g not in conteo_generos:
                conteo_generos[g] = 1
            else:
                conteo_generos[g] += 1
    print("Conteo por género:")
    for g, cantidad in conteo_generos.items():
        print("-", g, ":", cantidad)
#  **************** FIN FUNCIONES ******************** 

####################### PROGRAMA PRINCIPA ############################
# --- Crear el Diccionario ---
catalogo = {}
for titulo, anio, genero in juegos:
    clave = titulo.lower().replace(" ", "_")
    catalogo[clave] = {
        "titulo": titulo,
        "anio": anio,
        "genero": set(genero.split("/"))
    }
if __name__ == "__main__":
    # --- Menú principal ---
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ver catálogo")
        print("2. Crear juego")
        print("3. Leer juego (búsqueda exacta)")
        print("4. Buscar parcial")
        print("5. Buscar por género")
        print("6. Buscar por rango de años")
        print("7. Actualizar juego")
        print("8. Eliminar juego")
        print("9. Ver estadísticas")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            for clave, datos in catalogo.items():
                print(clave, ":", datos)
        elif opcion == "2":
            crear_juego(catalogo)
        elif opcion == "3":
            leer_juego(catalogo)
        elif opcion == "4":
            buscar_parcial(catalogo)
        elif opcion == "5":
            buscar_por_genero(catalogo)
        elif opcion == "6":
            buscar_por_rango(catalogo)
        elif opcion == "7":
            actualizar_juego(catalogo)
        elif opcion == "8":
            eliminar_juego(catalogo)
        elif opcion == "9":
            estadisticas(catalogo)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

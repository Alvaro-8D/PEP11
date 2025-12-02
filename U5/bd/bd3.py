import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
        )
    cursor = conexion.cursor()
    sql = "INSERT INTO series (titulo, genero) VALUES (%s, %s)"
    val = [
        ("Stranger Things", "Ciencia ficción"),
        ("The Office", "Comedia"),
        ("Game of Thrones", "Fantasía"),
        ("Sherlock", "Misterio"),
        ]
    cursor.executemany(sql, val)
    conexion.commit()
    print(cursor.rowcount, "filas se han insertado.")
    cursor.close()
    conexion.close()
except Error as e:
    print(f" Error con MySQL: {e}")
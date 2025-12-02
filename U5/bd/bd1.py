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
    cursor.execute(
    '''CREATE TABLE series (id INT AUTO_INCREMENT PRIMARY KEY, titulo
    VARCHAR(255) NOT NULL, genero VARCHAR(100));'''
    )
    cursor.close()
    conexion.close()
except Error as e:
    print(f" Error con MySQL: {e}")
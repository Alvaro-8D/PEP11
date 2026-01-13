import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host="localhost",
        user="planetas",
        password="planetas",
        database="planetas"
    )
    if con.is_connected():
        print("Conexión establecida correctamente\n")

    cur = con.cursor()
    cur.execute("""CREATE TABLE planetas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                tipo VARCHAR(50),
                lunas INT);""")
    print("Tabla creada correctamente\n")
    
    cur.execute("INSERT INTO planetas (nombre,tipo,lunas) VALUES ('Marte','rocosoooo',3)")
    cur.execute("INSERT INTO planetas (nombre,tipo,lunas) VALUES ('Jupiter','gaseoso',3)")
    print("Insercciones hechas correctamente\n")

    cur.execute("SELECT id,nombre,tipo,lunas FROM planetas WHERE id = 1")
    for n,p,pm in cur.fetchall():
        print(f"{n} - {p} ({pm} millones)")

    con.commit()
    con.close()
except Error as e:
    print("Error:", e)
finally:
    if 'con' in locals() and con.is_connected():
        con.close()
# programa04
# El módulo turtle es una biblioteca estándar de Python que permite crear gráficos y dibujos
# de manera sencilla, moviendo una “tortuga” virtual por la pantalla. El módulo está instalado
# por defecto en el intérprete de Python.
# Investiga la documentación del módulo https://docs.python.org/3/library/turtle.html y
# escribe un programa que:
# • Dibuje un cuadrado rojo sin rellenar.
# • Dibuje un círculo verde relleno.

import turtle
import tkinter

# Configurar la tortuga
t = turtle.Turtle()

# Dibujar cuadrado rojo sin rellenar
t.color("red")
for _ in range(4):
    t.forward(100)
    t.right(90)

# Mover a otra posición
t.penup()
t.goto(200, 0)
t.pendown()

# Dibujar círculo verde relleno
t.color("green", "green")
t.begin_fill()
t.circle(50)
t.end_fill()

# Mantener la ventana abierta hasta que el usuario la cierre
turtle.done()

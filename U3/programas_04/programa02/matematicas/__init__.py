# Fichero __init__.py

__version__ = "1.0"
__author__ = "Álvaro"
__all__ = [
    "a_binario","a_hexadecimal","a_entero",
    "area_rectangulo","area_triangulo","area_circulo",
    "suma","resta","multiplicacion","division",
]

print("\nInicializando mi paquete....")

from .conversiones import a_binario, a_hexadecimal, a_entero
from .figuras import area_rectangulo, area_triangulo, area_circulo
from .operaciones import suma, resta, multiplicacion, division






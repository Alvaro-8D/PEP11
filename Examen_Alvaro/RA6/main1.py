from abc import ABC, abstractmethod


class Producto(ABC): # Indica que es una Clase ABSTRACTA

    def __init__(self, nombre, precios):
        self.__nombre = nombre
        self.__precios = precios

    @property
    def nombre(self, nombre):
        return self.__nombre
    
    @property
    def precio_actual(self):
        return self.__precios
    
    def añadir_precio(self, precio):
        if precio > 0:
            self.__precios[len(self.__precios)] = precio
            
    @abstractmethod
    def calcular_precio_final(self):
        return self.__precios[len(self.__precios)-1]


class DiscoDuro(Producto):
    def __init__(self, nombre, precios ,tipo):
        super().__init__(nombre, precios)
        self.tipo = tipo
    
    def calcular_precio_final(self):
        if self.__nombre == "SSD":
            self.__precios[len(self.__precios)-1] = self.__precios[len(self.__precios)-1]*(1.20) # +20%

        return self.__precios[len(self.__precios)-1]
    

class Memoria(Producto):
    def __init__(self, nombre, precios ,capacidad):
        super().__init__(nombre, precios)
        self.capacidad = capacidad

    def __str__(self):
        return f"{self.__class__.__name__}(nombre='{self.nombre}', Capacidad={self.capacidad})"

    def calcular_precio_final(self):
        if self.capacidad == 16:
            self.__precios[len(self.__precios)-1] = self.__precios[len(self.__precios)-1]*(1.50) # +50%

        return self.__precios[len(self.__precios)-1]
    
def main():
    d1 = DiscoDuro("Disco super chulo",[10,22,15],"HDD")
    m1 = Memoria("Memoria super grande",[23,55,143],32)

    inventario = [d1,m1]

    print(d1.nombre())

if __name__ == "__main__":
    main()
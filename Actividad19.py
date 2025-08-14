#Se crea clase de galletas
class Galleta:
    def __init__(self, nombre, precio, peso):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso

    #Funcion para mostrar la informacion
    def mostrar_info(self):
        return self.nombre + "|  Q" + str(self.precio) + " | " + str(self.peso) + "g"


# Clase para galletas con chispas la cual sera heredada de Gallea
class GalletaChispas(Galleta):
    def __init__(self, nombre, precio, peso, chispas):
        Galleta.__init__(self, nombre, precio, peso)
        self.chispas = chispas

    def mostrar_info(self):
        return self.nombre + "| Q" + str(self.precio) + " | " + str(self.peso) + "g" + " | Chispas: " + str(self.chispas)

#Clase para el relleno
class Relleno:
    def __init__(self, sabor):
        self.sabor = sabor

    def tipo_relleno(self):
        return "Relleno de " + self.sabor

#Clase de la galleta rellena que heredara dos clases, la de galleta y la de relleno
class GalletaRellena(Galleta, Relleno):
    def __init__(self, nombre, precio, peso, sabor):
        Galleta.__init__(self, nombre, precio, peso)
        Relleno.__init__(self, sabor)

    def mostrar_info(self):
        return self.nombre + " | Q" + str(self.precio) + " | " + str(self.peso) + "g | " + self.tipo_relleno()



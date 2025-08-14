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

class RegistrarGalleta:
    def __init__(self):
        self.galletas = []

    # función para verificar si un nombre ya existe
    def existe_nombre(self, nombre):
        for i in self.galletas:
            if i.nombre.lower() == nombre.lower():
                return True
        return False

    # funcion para registrar galleta basica
    def registrar_basica(self):
        nombre = input("Nombre: ")
        if self.existe_nombre(nombre):
            print("Ya existe una galleta con ese nombre.")
            return
        try:
            precio = float(input("Precio: "))
            peso = float(input("Peso: "))
        except:
            print("Error: debes poner numeros en precio y peso.")
            return
        i = Galleta(nombre, precio, peso)
        self.galletas.append(i)
        print("Galleta registrada.")

    # funcion para registrar galleta con chispas
    def registrar_chispas(self):
        nombre = input("Nombre: ")
        if self.existe_nombre(nombre):
            print("Ya existe una galleta con ese nombre.")
            return
        try:
            precio = float(input("Precio: "))
            peso = float(input("Peso: "))
            chispas = int(input("Cantidad de chispas: "))
        except:
            print("Error: debes poner numeros válidos.")
            return
        i = GalletaChispas(nombre, precio, peso, chispas)
        self.galletas.append(i)
        print("Galleta registrada.")

    # funcion para registrar galleta rellena
    def registrar_rellena(self):
        nombre = input("Nombre: ")
        if self.existe_nombre(nombre):
            print("Ya existe una galleta con ese nombre.")
            return
        try:
            precio = float(input("Precio: "))
            peso = float(input("Peso: "))
        except:
            print("Error: debes poner numeros en precio y peso.")
            return
        sabor = input("Sabor del relleno: ")
        i = GalletaRellena(nombre, precio, peso, sabor)
        self.galletas.append(i)
        print("Galleta registrada.")

    # funcion para registrar galleta
    def listar_galletas(self):
        if len(self.galletas) == 0:
            print("No hay galletas.")
        else:
            for i in self.galletas:
                print(i.mostrar_info())

    # funcion para buscar galleta
    def buscar_galleta(self):
        nombre = input("Nombre a buscar: ")
        encontrada = False
        for g in self.galletas:
            if g.nombre.lower() == nombre.lower():
                print(g.mostrar_info())
                encontrada = True
        if not encontrada:
            print("No se encontró.")

    # funcion para eliminar galleta
    def eliminar_galleta(self):
        nombre = input("Nombre a eliminar: ")
        for g in self.galletas:
            if g.nombre.lower() == nombre.lower():
                self.galletas.remove(g)
                print("Galleta eliminada.")
                return
        print("No se encontró.")

registrar = RegistrarGalleta()
while True:
  try:
    print("\n--- MENÚ ---")
    print("1. Registrar galleta básica")
    print("2. Registrar galleta con chispas")
    print("3. Registrar galleta rellena")
    print("4. Listar galletas")
    print("5. Buscar galleta")
    print("6. Eliminar galleta")
    print("7. Salir")

    try:
        opcion = int(input("Elija una opcion: "))
    except ValueError:
        print("Ingrese un numero valido")
    except TypeError:
        print("Ingrese un numero valido")

    if opcion == 1:
        registrar.registrar_basica()
    elif opcion == 2:
        registrar.registrar_chispas()
    elif opcion == 3:
        registrar.registrar_rellena()
    elif opcion == 4:
        registrar.listar_galletas()
    elif opcion == 5:
        registrar.buscar_galleta()
    elif opcion == 6:
        registrar.eliminar_galleta()
    elif opcion == 7:
        print("Cerrando Programa :)")
        break
    else:
        print("Opcion no válida.")

  except Exception as e:
      print("Ocurrio un error inesperado.")
### CLASES
class Productos:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def __repr__(self):
        return "nombre Producto: {}, cantidad: {}".format(self.nombre, self.cantidad)
    
class Perecedero(Productos):
    def __init__(self, nombre, cantidad, diasCaducar):
        Productos.__init__(self, nombre, cantidad)
        self.diasCaducar = diasCaducar
    def __repr__(self):
        return "nombre Producto: {}, cantidad: {}, dias a caducar: {}".format(self.nombre, self.cantidad,self.diasCaducar)

    def calcular(self, productosADonar, cantidadEntidades):
        productosPorEntidad = self.cantidad // cantidadEntidades
        if productosADonar <= self.cantidad:
            productoPorEntidad = productosADonar // cantidadEntidades
            print("Se enviaran {} a entidades".format(productoPorEntidad))
            print("Voy a donar")
        else:
            print("no alcanza para todos")

class Noperecedero(Productos):
    def __init__(self, nombre, cantidad, tipo):
        Productos.__init__(self, nombre, cantidad)
        self.tipo = tipo

#def Calcular():


###CODIGO PRINCIPAL
perecedero = Perecedero("Mate",45,5)
noper1 = Noperecedero("Remera",45,5)
print(perecedero)

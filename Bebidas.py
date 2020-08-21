###CLASES
class Almacen:
    def __init__(self,nombre):
        self.nombre = nombre
        

class Bebidas:
    def __init__(self, id, cantidadLitros, precio, marca):
        self.id = id
        self.cantidadLitros = cantidadLitros
        self.precio = precio
        self.marca = marca

    def calcularPrecioBebidas(self,precio,precio2):
        total = total + self.precio
        print(total)

class aguaMineral(Bebidas):
    def __init__(self,id,cantidadLitros,precio,marca,origen):
        Bebidas.__init__(self,id,cantidadLitros,precio,marca)
        self.origen = origen
        
    def __repr__(self):
        return "ID Producto: {}, cantidad Litros: {}, Precio:$ {}, marca: {}, Origen: {}".format(self.id, self.cantidadLitros,self.precio,self.marca,self.origen)

class Gaseosas(Bebidas):
    def __init__(self,id,cantidadLitros,precio,marca,porcentajeAzucar,promocion,descuento = 0):
        Bebidas.__init__(self,id,cantidadLitros,precio,marca)
        self.porcentajeAzucar = porcentajeAzucar
        self.promocion = promocion
        self.descuento = descuento
        if self.promocion == "SI":
            self.descuento = self.precio - (self.precio * 10 / 100)
        elif self.promocion == "NO":
            self.descuento = 0
        

    def __repr__(self):
        return "ID Producto: {}, cantidad Litros: {}, Precio: ${}, Marca: {}, Porcentaje Azucar {}%, Promocion: {}, Precio con Descuento: ${}".format(self.id, self.cantidadLitros,self.precio,self.marca,self.porcentajeAzucar,self.promocion,self.descuento)

### METODOS


###CODIGO PRINCIPAL
agua = aguaMineral(1234,5,34,"aguas del Rey","ciudad")
agua2 = aguaMineral(12345,6,45,"ivess","manantial")
gaseosa = Gaseosas(123,4,100,"cocacola",100,"NO")
gaseosa2= Gaseosas(12,4,150,"pepsi",150,"NO")
print(gaseosa2.precio)
Bebidas.calcularPrecioBebidas(agua,agua2)
#print(total)
print(agua)
print(agua2)
print(gaseosa)
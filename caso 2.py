class Vehiculo:
    def __init__(self, color,ruedas):
        self.color = color
        self.ruedas = ruedas
    
class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindradas):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas,carga):
        self.carga = carga

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        self.tipo = tipo

class motocicleta(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindradas):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas

##FUNCIONES
def catalogar(cat):
    for i in range(0,len(cat)):
        print(cat[i])

##CODIGO PRINCIPAL
vehiculo = []
moto = ("rojo", 2, 1000,50)
coche = ("azul", 4, 100, 200)
bici = ("negro",2,"montanbike")
camioneta = ("gris", 4, 1000)
vehiculo.append(moto)
vehiculo.append(coche)
vehiculo.append(bici)
vehiculo.append(camioneta)
catalogar(vehiculo)

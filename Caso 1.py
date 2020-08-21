class Vehiculo:
    def __init__(self, color,ruedas):
        self.color = color
        self.ruedas = ruedas
    
class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindradas):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas

vehiculo1 = ("rojo", 4)
coche1 = ("verde", 4, 100, 500)

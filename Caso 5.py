class Tiempo:
    def __init__(self, hora, minutos=0, segundos=0):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos
    
    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.hora,self.minutos,self.segundos)
    
tiempoHMS = Tiempo(1,34,44)
print(tiempoHMS)
tiempoHM = Tiempo(11,20)
print(tiempoHM)
tiempoH = Tiempo(4)
print(tiempoH)

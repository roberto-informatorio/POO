from random import shuffle

class Carta:
    def __init__(self,figura,valor):
        self.figura = figura
        self.valor = valor

    def __repr__(self):
        return "{} de {}".format(self.valor,self.figura)

class baraja:
    def __init__(self):
        figuras = ['Espadas','Copas','Bastos','Oro']
        valores = ['1','2','3','4','5','6','7','Sota','Caballo','Rey']
        self.cartas = [Carta(figura,valor)for figura in figuras for valor in valores]
        self.descarte = list()
    
    def barajar(self):
        return shuffle(self.cartas)
    
    def siguienteCarta(self):
        if (len(self.cartas) == 0):
            raise ValueError("Todas las cartas se repartieron")
        cartaRepartida = self.cartas.pop()
        self.descarte.append(cartaRepartida)
        return cartaRepartida

    def cartasDisponibles(self):
        return len(self.cartas)

    def darCartas(self, cantidad):
        if (self.cartasDisponibles() < cantidad):
              raise ValueError("No dispongo de cartas suficientes para satisfacer la solicitud")
        print("Estas son sus ", cantidad, "cartas:")
        for _ in range(cantidad):
            cartaRepartida = self.cartas.pop()
            print(cartaRepartida())
    
    def cartasMonton(self):
        if (len(self.descarte) == 0):
            print("Todavia no se repartio ninguna carta")
        return self.descarte
        
    def mostrarBaraja(self):
        print(self.cartas)

    def __repr__(self):
        return "Cartas: {}".format(self.cartas)


### CODIGO PRINCIPAL
carta = Carta("Copa","6")
print(carta)

baraja = baraja()
print(baraja)
print("*"*20)
baraja.barajar()
print(baraja)
print(baraja.siguienteCarta())
print(baraja.cartasDisponibles())
baraja.darCartas(3)
print(baraja.cartasDisponibles())
print(baraja.cartasMonton())
baraja.mostrarBaraja()
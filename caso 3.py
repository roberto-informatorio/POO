class Triangulo:
    def __init__(self):
        self.lado1 = int(input("ingrese lado 1:"))
        self.lado2 = int(input("ingrese lado 2:"))
        self.lado3 = int(input("ingrese lado 3:"))
    
    def mayor(self):
        if self.lado1 > self.lado2 and self.lado1 and self.lado1 > lado3:
            print("El mayor de los lados ingresados es lado 1: ", lado1)
        elif self.lado2>self.lado3:
            print("El mayor de los lados ingresados es el lado 2: ", lado2)
        else:
            print("El lado mayor de los lados ingresados es el lado 3: ", lado3)
    
    def tipo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Es un triangulo equilatero")
        elif self.lado1 == self.lado2 and self.lado1 != self.lado3:
            print("Es un triangulo escaleno")
        else:
            print("Es un triangulo isoceles")


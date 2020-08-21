class Cuenta:
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        print("Titular Cuenta: {}".format(self.titular))
        print("Cantidad de dinero: $", self.cantidad)
    

    def ingresar(self, cantidad):
        if cantidad < 0:
            print("monto ingresado negativo")
        self.cantidad = self.cantidad + cantidad
        

    def retirar(self, cantidad):
        if cantidad < self.cantidad:
            print("Cuenta en rojo")
        self.cantidad = self.cantidad - cantidad


###CODIGO PRINCIPAL
cuenta1= Cuenta("Roberto",300)

cuenta1.ingresar(700)
cuenta1.retirar(1000)
cuenta1.mostrar()

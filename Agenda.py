#### AGENDA V2
 
## ESPACIO DE CLASES
class Agenda:
 
   def __init__(self, nombreAgenda):
       self.nombre = nombreAgenda
       self.contactos = list()
 
   def agregarContacto(self, contacto):
       self.contactos.append(contacto)
 
class Contacto:
   def __init__(self, nombre, apellido):
       self.nombre = nombre
       self.apellido = apellido
  
   def __repr__(self):
       return "{} {}".format(self.nombre, self.apellido)
 
## CODIGO PRINCIPAL
agenda = Agenda("Agenda Android")
print(agenda)
print(agenda.nombre)
print(agenda.contactos)
agenda.agregarContacto(Contacto("Juan", "Perez"))
agenda.agregarContacto(Contacto("Carlos", "Gomez"))
print(agenda.contactos)
print(agenda.contactos[0])

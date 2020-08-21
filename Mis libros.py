###CLASES
class Libros:
    def __init__(self, titulo, autor,nroPaginas):
        self.titulo = titulo
        self.autor = autor
        self.nroPaginas = nroPaginas
    
    def __repr__(self):
        return "Titulo Libro: {} Autor: {} Numero de Paginas: {}".format(self.titulo, self.autor,self.nroPaginas)

    

###CODIGO PRINCIPAL
libro1 = Libros("Tiburon","Mercedes",300)
print(libro1)
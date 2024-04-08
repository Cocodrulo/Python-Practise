class Libro:
    def __init__(self, titulo, isbn):
       self.__titulo = ""
       self.titulo = titulo
       self.__isbn = ""
       self.isbn = isbn
    
    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, n_isbn):
        self.__isbn = n_isbn
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, n_titulo):
        self.__titulo = n_titulo
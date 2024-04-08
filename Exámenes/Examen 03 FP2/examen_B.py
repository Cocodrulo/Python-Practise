from clases import Libro
import functools


@functools.total_ordering
class LibroElectronico(Libro):
    def __init__(self, titulo, isbn, url):
        super().__init__(titulo, isbn)
        self.__url = ""
        self.url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, n_url):
        self.__url = n_url

    def __eq__(self, other):
        if not isinstance(other, LibroElectronico):
            return False
        return self.titulo == other.titulo and self.isbn == other.isbn

    def __gt__(self, other):
        if not isinstance(other, LibroElectronico):
            return False
        return self.titulo > other.titulo or (self.titulo == other.titulo and
                                              self.isbn > other.isbn) 
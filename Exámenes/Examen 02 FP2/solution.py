"""Module with the answer to the problem."""


# CREE AQUÍ SU CLASE Texto
class Texto:
    def __init__(self, paragraphs):
        self.__paragraphs = paragraphs
        self.__nparrafos = len(paragraphs)
        self.__npalabras = contar_palabras(paragraphs)

    @property
    def npalabras(self):
        return self.__npalabras

    @property
    def nparrafos(self, index):
        return self.__npalabras[index]

    @nparrafos.setter
    def nparrafos(self, value):
        diff = value - self.__nparrafos
        if diff == 0:
            return
        elif diff < 0:
            self.__paragraphs[:diff]
        elif diff > 0:
            self.__paragraphs += [Parrafo("") for num in range(diff)]
        self.__npalabras = contar_palabras(self.__paragraphs)
        self.__nparrafos += diff

    def get_parrafo(self, index):
        return self.__paragraphs[index]

    def set_parrafo(self, index, newparagraphs):
        self.__paragraphs[index] = newparagraphs
        self.npalabras = contar_palabras(self.__paragraphs)

    def __str__(self):
        return "\n".join([x.get_str() for x in self.__paragraphs])

def contar_palabras(texto):
    return sum([len(parrafo.get_palabras) for parrafo in texto])
# NO MODIFIQUE EL CODIGO DEBAJO DE ESTA LINEA


class Parrafo:
    """Representa un párrafo."""

    def __init__(self, texto):
        """Se inicializa un párrafo al texto str pasado."""
        if type(texto) != str:
            raise ValueError
        self.__contenido = texto

    def get_palabras(self):
        """Devuelve una lista con las palabras en el párrafo."""
        import re
        return re.findall(r"\b\w+\b", self.__contenido)

    def get_ncaracteres(self):
        """Devuelve el número de caracteres en las palabras del párrafo."""
        return sum([len(p) for p in self.get_palabras()])

    def get_str(self):
        """Devuelve la representación informal del párrafo."""
        return self.__contenido
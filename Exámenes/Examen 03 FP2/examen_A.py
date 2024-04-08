"""Clase a modificar el ejercicio."""

class Botella:
    """Representa una botella con una determinada capacidad y contenido."""
    capacidades = {200, 500, 800}

    def __init__(self, capacidad, contenido):
        if capacidad not in self.__class__.capacidades:
            raise ValueError("capacidad")
        self.__capacidad = capacidad
        self.__contenido = contenido
    
    @classmethod
    def nueva_capacidad(cls, capacidad):
        if type(capacidad) != int:
            raise TypeError("nueva capacidad")
        cls.capacidades.add(capacidad)

    @property
    def capacidad(self):
        return self.__capacidad

    @property
    def contenido(self):
        return self.__contenido

    @contenido.setter
    def contenido(self, nuevo_contenido):
        self.__contenido = nuevo_contenido

if __name__ == "__main__":
    tests = [(500, 200), (20, 1), (34, 100), (20, 20)]
    for i in tests:
        try:
            print("==== TEST ====")
            botella = Botella(i[0], i[1])
            print("Capacidad:", botella.capacidad, "Contenido:", botella.contenido)
            botella.contenido = 50
            print("Capacidad:", botella.capacidad, "Contenido:", botella.contenido)
            print(botella.capacidades)
            Botella(200, 65)
            print("Hay ",botella.botellas_capacidad(200), "de 200 cc")
        except Exception as err:
            print("Ha ocurrido el error ", type(err).__name__, " con el mensaje \"", err, "\"", sep="")
        
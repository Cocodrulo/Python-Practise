"""Ejemplo de uso de la funciones requerida."""

from solution import Texto, Parrafo

poema0 = ['Hola ola', "no te decides"]

poema1 = [
    "La tierra estaba seca.",
    "No había ríos ni fuentes.",
    "Y brotó de tus ojos",
    "el agua, toda el agua."
]
poema2 = [
    "Ante las puertas bien cerradas,",
    "Sobre un río de olvido, va la canción antigua.",
    "Una luz lejos piensa",
    "Como a través de un cielo.",
    "Todos acaso duermen",
    "Mientras él lleva su destino a solas."
]

poemas = []
poemas.append(poema0)
# poemas.append(poema1) # Descomente si quiere probar otro texto
# poemas.append(poema2)  # Descomente si quiere probar otro texto

for poema in poemas:
    parrafos = [Parrafo(ristra) for ristra in poema]
    print("Datos", poema)
    t = Texto(parrafos)
    print("nparrafos", t.nparrafos)
    print("npalabras", t.npalabras)
    pos = len(poema) // 2
    print(f"get_parrafo {pos}", t.get_parrafo(pos).get_str())
    print("Representación informal", t)
    t.set_parrafo(pos, Parrafo("Núevo párrafo"))
    print(f"set_parrafo {pos}", t.get_parrafo(pos).get_str())
    print("nparrafos", t.nparrafos)
    print("npalabras", t.npalabras)
    print("Representación informal", t)
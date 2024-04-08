from solucion import StringsPrinter as sol
from template import StringsPrinter

if __name__ == "__main__":
    test = []
    test.append(["2", 2, True, 9, "hola", "Adiós", 9.26, "4.74", "javier", "Sara", None])
    test.append(["2", 2, True, 9, "chao", "Cuandp", 9.26, "4.74", "None", "", None])
    results = []

    for i, x in enumerate(test):
        try:
            print("============================")
            print(f"Realizando test {i}")
            print("============================")
            print()
            solution = sol(x)
            for s in StringsPrinter(x):
                print(f"Valor: {s}")
                results.append(s == next(solution))
        except Exception:
            results.append(False)

    resultados = results.count(True)
    print(f"Resultados: {resultados}/{len(results)}")
